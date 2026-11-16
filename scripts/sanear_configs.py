#!/usr/bin/env python3
"""
Saneo de secretos en configuraciones de red antes de subirlas al repo.

Reemplaza contraseñas, hashes, claves precompartidas (PSK), claves de
TACACS+/RADIUS/OSPF/BGP/HSRP/NTP y comunidades SNMP por <SANEADO>.

Cubre: Cisco IOS / IOS-XE, FortiOS, VyOS (formato "set" y formato con llaves)
y pfSense (config.xml).

Uso:
    # Una config: de privado/ a la carpeta del capítulo
    python scripts/sanear_configs.py privado/cap01/GARAGE-RT.txt docs/capitulos/cap01-garage/configs/LL-GAR-RT-EDGE01.txt

    # Una carpeta completa (recursivo, respeta la estructura)
    python scripts/sanear_configs.py privado/cap01 docs/capitulos/cap01-garage/configs

    # Solo mostrar el resultado por pantalla
    python scripts/sanear_configs.py privado/cap01/GARAGE-RT.txt

    # Verificar que no quede ningún secreto (lo usa el CI; devuelve 1 si encuentra algo)
    python scripts/sanear_configs.py --verificar docs

Limitaciones conocidas (revisá a ojo antes de subir):
  - FortiOS: la comunidad SNMP se define con "set name" dentro de
    "config system snmp community", y "set name" se usa en todos lados,
    así que no se detecta automáticamente.
  - Secretos que aparezcan en texto libre (descripciones, banners, comentarios).
  - Formatos de otros fabricantes no listados arriba.
El script reduce el riesgo; no reemplaza mirar el diff antes del commit.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARCA = "<SANEADO>"

# Valor de un secreto: entre comillas simples, dobles, o una palabra sin espacios.
VALOR = r"""('[^']*'|"[^"]*"|\S+)"""
# Tipo de cifrado opcional de IOS (0, 5, 6, 7, 8, 9).
TIPO = r"(?:\s+[0-9])?"

# (nombre, regex). El grupo 1 es lo que se conserva; el grupo 2 es el secreto.
REGLAS_LINEA: list[tuple[str, re.Pattern[str]]] = [
    # ---------- Cisco IOS / IOS-XE ----------
    ("ios-enable", rf"^(\s*enable\s+(?:secret|password)(?:\s+level\s+\d+)?{TIPO}\s+){VALOR}"),
    ("ios-username", rf"^(\s*username\s+\S+.*?\s(?:secret|password){TIPO}\s+){VALOR}"),
    ("ios-line-password", rf"^(\s*password{TIPO}\s+){VALOR}"),
    ("ios-snmp-community", rf"^(\s*snmp-server\s+community\s+){VALOR}"),
    ("ios-isakmp-key", rf"^(\s*crypto\s+isakmp\s+key{TIPO}\s+){VALOR}"),
    ("ios-ikev2-psk", rf"^(\s*pre-shared-key(?:\s+(?:local|remote))?{TIPO}\s+){VALOR}"),
    ("ios-aaa-server-key", rf"^(\s*(?:tacacs|radius)-server\s+(?:host\s+\S+.*?\s)?key{TIPO}\s+){VALOR}"),
    ("ios-server-private-key", rf"^(\s*server-private\s+\S+.*?\skey{TIPO}\s+){VALOR}"),
    # "key 7 xxxx" dentro de "tacacs server X"; no toca "key 1" ni "key chain NOMBRE".
    ("ios-key", rf"^(\s*key\s+(?:[0-9]\s+)?)(?!\d+\s*$)(?!chain\b|config-key\b){VALOR}"),
    ("ios-key-string", rf"^(\s*key-string{TIPO}\s+){VALOR}"),
    ("ios-hsrp-md5", rf"^(\s*standby\s+\d+\s+authentication\s+md5\s+key-string{TIPO}\s+){VALOR}"),
    ("ios-ospf-auth-key", rf"^(\s*ip\s+ospf\s+authentication-key{TIPO}\s+){VALOR}"),
    ("ios-ospf-md5", rf"^(\s*ip\s+ospf\s+message-digest-key\s+\d+\s+md5{TIPO}\s+){VALOR}"),
    ("ios-bgp-password", rf"^(\s*neighbor\s+\S+\s+password{TIPO}\s+){VALOR}"),
    ("ios-ntp-key", rf"^(\s*ntp\s+authentication-key\s+\d+\s+md5\s+){VALOR}"),
    ("ios-hsrp-text", rf"^(\s*standby\s+\d+\s+authentication\s+(?:text\s+)?)(?!md5\b){VALOR}"),
    ("ios-wpa-psk", rf"^(\s*wpa-psk\s+ascii{TIPO}\s+){VALOR}"),
    # ---------- FortiOS ----------
    (
        "fortios-set-secreto",
        r"^(\s*set\s+(?:psksecret|password|passwd|secret|key|auth-pwd|priv-pwd|"
        r"passphrase|sae-password|private-key|ppk-secret)\s+)(.+)$",
    ),
    # ---------- VyOS ----------
    (
        "vyos-set-secreto",
        rf"^(\s*set\s.*?\s(?:secret|pre-shared-secret|plaintext-password|"
        rf"encrypted-password|password|key|private-key|preshared-key)\s+){VALOR}",
    ),
    ("vyos-set-snmp-community", rf"^(\s*set\s+service\s+snmp\s+community\s+){VALOR}"),
    (
        "vyos-llaves-secreto",
        rf"^(\s*(?:secret|pre-shared-secret|plaintext-password|encrypted-password)\s+){VALOR}",
    ),
    ("vyos-llaves-snmp-community", rf"^(\s*community\s+){VALOR}(?=\s*\{{)"),
]
REGLAS_LINEA = [(n, re.compile(r, re.IGNORECASE)) for n, r in REGLAS_LINEA]

# pfSense config.xml: el contenido de estas etiquetas es secreto.
ETIQUETAS_XML = [
    "password", "bcrypt-hash", "sha512-hash", "pre-shared-key", "rocommunity",
    "rwcommunity", "community", "prv", "secret", "passwd", "shared_key", "tls",
]
REGLA_XML = re.compile(
    r"(<(" + "|".join(ETIQUETAS_XML) + r")>)([^<]+)(</\2>)", re.IGNORECASE
)

EXTENSIONES_TEXTO = {".txt", ".cfg", ".conf", ".config", ".log", ".xml", ".md", ".boot", ""}


def ya_saneado(valor: str) -> bool:
    v = valor.strip().strip("'\"")
    return v.startswith("<") and v.endswith(">")


def sanear_texto(texto: str) -> tuple[str, list[tuple[int, str]]]:
    """Devuelve (texto_saneado, [(número_de_línea, regla), ...])."""
    hallazgos: list[tuple[int, str]] = []
    salida = []
    for n, linea in enumerate(texto.splitlines(keepends=True), start=1):
        for nombre, regla in REGLAS_LINEA:
            m = regla.search(linea)
            if m and not ya_saneado(m.group(2)):
                fin = "\n" if linea.endswith("\n") else ""
                resto = linea[m.end(2):].rstrip("\n")
                linea = m.group(1) + MARCA + resto + fin
                hallazgos.append((n, nombre))
        nueva, cantidad = REGLA_XML.subn(
            lambda m: m.group(3) if ya_saneado(m.group(3))
            else m.group(1) + MARCA + m.group(4),
            linea,
        )
        if nueva != linea:
            hallazgos.append((n, "pfsense-xml"))
            linea = nueva
        salida.append(linea)
    return "".join(salida), hallazgos


def archivos(ruta: Path):
    if ruta.is_file():
        yield ruta
        return
    for p in sorted(ruta.rglob("*")):
        if p.is_file() and p.suffix.lower() in EXTENSIONES_TEXTO:
            yield p


def leer(p: Path) -> str | None:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return p.read_text(encoding="latin-1")
        except Exception:
            return None


def verificar(ruta: Path) -> int:
    total = 0
    for p in archivos(ruta):
        texto = leer(p)
        if texto is None:
            continue
        _, hallazgos = sanear_texto(texto)
        for n, regla in hallazgos:
            print(f"SECRETO  {p}:{n}  ({regla})")
            total += 1
    if total:
        print(f"\n{total} posible(s) secreto(s) sin sanear. Pasá esos archivos por el script.", file=sys.stderr)
        return 1
    print("OK: no se encontraron secretos sin sanear.", file=sys.stderr)
    return 0


def sanear(entrada: Path, salida: Path | None) -> int:
    if entrada.is_dir() and salida is None:
        print("Para sanear una carpeta indicá la carpeta de salida.", file=sys.stderr)
        return 2
    for p in archivos(entrada):
        texto = leer(p)
        if texto is None:
            print(f"Omitido (no es texto): {p}", file=sys.stderr)
            continue
        limpio, hallazgos = sanear_texto(texto)
        if salida is None:
            sys.stdout.write(limpio)
        else:
            destino = salida / p.relative_to(entrada) if entrada.is_dir() else salida
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(limpio, encoding="utf-8")
            print(f"{p} -> {destino}", file=sys.stderr)
        for n, regla in hallazgos:
            print(f"  línea {n}: {regla}", file=sys.stderr)
        print(f"  {len(hallazgos)} secreto(s) reemplazado(s)", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada", type=Path, help="archivo o carpeta de entrada")
    ap.add_argument("salida", type=Path, nargs="?", help="archivo o carpeta de salida (si se omite, imprime)")
    ap.add_argument("--verificar", action="store_true", help="solo buscar secretos; sale con 1 si hay alguno")
    args = ap.parse_args()
    if not args.entrada.exists():
        print(f"No existe: {args.entrada}", file=sys.stderr)
        return 2
    if args.verificar:
        return verificar(args.entrada)
    return sanear(args.entrada, args.salida)


if __name__ == "__main__":
    sys.exit(main())

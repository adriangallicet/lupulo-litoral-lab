#!/usr/bin/env bash
# Crea las etiquetas de Issues del proyecto (prioridad, sede, tipo, capítulo).
# Requiere GitHub CLI autenticado:  gh auth login
# Uso:  bash scripts/crear_etiquetas.sh
# Es idempotente: si la etiqueta existe, la actualiza (--force).
set -euo pipefail

REPO="adriangallicet/lupulo-litoral-lab"

e() { gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force; }

# Prioridad (criterio en docs/referencia/estandar-documentacion.md)
e "P1" "b60205" "Crítico: servicio caído para el negocio (no se cobra, no se produce)"
e "P2" "d93f0b" "Alto: servicio degradado o una sede afectada"
e "P3" "fbca04" "Medio: molestia con alternativa disponible"
e "P4" "c2e0c6" "Bajo: mejora, consulta o pendiente sin impacto"

# Tipo (ITIL)
e "incidente" "e11d21" "Restablecer un servicio que dejó de funcionar"
e "problema"  "5319e7" "Causa raíz de incidentes repetidos"
e "cambio"    "0052cc" "Modificación planificada"
e "docs"      "0075ca" "Documentación"

# Sede
e "sede:garage"     "f9d0c4" "Garage original"
e "sede:bar"        "f9d0c4" "Taproom / bares"
e "sede:planta"     "f9d0c4" "Planta industrial"
e "sede:gualeguaychu" "f9d0c4" "Sucursal Gualeguaychú"
e "sede:parana"     "f9d0c4" "Sucursal Paraná"
e "sede:todas"      "f9d0c4" "Afecta a toda la empresa"

# Capítulo
for n in 00 01 02 03 04 05 06 07; do
  e "cap:$n" "ededed" "Capítulo $n"
done

echo "Etiquetas listas."

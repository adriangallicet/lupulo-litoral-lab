# Lúpulo Litoral — Home-lab de redes

Un home-lab de redes contado como una historia: una cervecería artesanal ficticia crece desde un garage en Concepción del Uruguay hasta una empresa con planta, bares y clientes grandes, y yo soy su consultor de redes. Cada capítulo es un pedido del cliente resuelto en el lab y documentado como un trabajo real.

**Sitio:** https://adriangallicet.github.io/lupulo-litoral-lab/

| Capítulo | Temas | Estado |
| --- | --- | --- |
| 0. Preparación | Repo, estándar de documentación, plantillas | En curso |
| 1. El garage | SSH, DHCP, NAT, IPv6, rutas estáticas | Pendiente |
| 2. El primer bar | VLAN, inter-VLAN, WLC, seguridad de LAN, ACL | Pendiente |
| 3. La planta | IT/OT, STP, EtherChannel, HSRP | Pendiente |
| 4. Las sucursales | OSPF, VPN IPsec multivendor | Pendiente |
| 5. Dos proveedores | BGP, route-maps, SD-WAN | Pendiente |
| 6. Nos auditan | TACACS+, syslog, NTP, hardening | Pendiente |
| 7. Ya somos empresa | Monitoreo, automatización, guardias | Pendiente |

## Trabajar en el repo

```bash
# Ver el sitio en local (http://127.0.0.1:8000)
pip install -r requirements.txt
mkdocs serve

# Sanear una config antes de subirla (las crudas van en privado/, que git ignora)
python scripts/sanear_configs.py privado/cap01/router.txt docs/capitulos/cap01-garage/configs/LL-GAR-RT-EDGE01.txt

# Verificar que no quede ningún secreto (lo mismo que corre el CI)
python scripts/sanear_configs.py --verificar docs
```

Convenciones completas: [`docs/referencia/estandar-documentacion.md`](docs/referencia/estandar-documentacion.md).

## Summary (English)

A hands-on networking home-lab framed as a story: a fictional brewery grows from a garage into a multi-site company and I am its network consultant. Each chapter is solved in Packet Tracer or EVE-NG and documented like real work, with design decisions, sanitized configs, packet captures and troubleshooting tickets. The documentation site is built with Material for MkDocs and published to GitHub Pages.

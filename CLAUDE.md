# Notas para Claude

Repo del home-lab "Lúpulo Litoral" de Adrián Gallicet. Lo que se publica vive en `docs/` (Material for MkDocs, ver ADR-001).

- Seguí `docs/referencia/estandar-documentacion.md`: nombres de equipos, commits `tipo(sede): descripción LL-NN` (clave de Jira), documentación en español con resumen en inglés.
- Adrián está aprendiendo: en los capítulos, guiá con pistas antes de dar soluciones completas, salvo que las pida. No asumas experiencia en routing dinámico, firewalls de producción, VPN, SD-WAN, TACACS+ ni MPLS.
- Nunca subas secretos. Configs crudas en `privado/`; publicar solo lo que pasó por `scripts/sanear_configs.py`.
- Antes de commitear: `mkdocs build --strict` y `python scripts/sanear_configs.py --verificar docs`.
- Al cerrar un ticket: agregar su fila en `docs/tickets/index.md`. Al crear un ADR: agregarlo en `docs/decisiones/index.md` y en `nav` de `mkdocs.yml`.

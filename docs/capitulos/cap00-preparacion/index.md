---
tags:
  - cap00
  - documentacion
  - git
---

# 0. Preparación

!!! note "Estado: en curso · Inicio: 2026-11-16"

## El llamado

Antes de ir al garage, armás tu valija de herramientas: un entorno de trabajo, un repo ordenado y una forma de documentar que puedas sostener durante todo el proyecto.

## Núcleo

- [x] Crear el repo `lupulo-litoral-lab` con su estructura y una página de presentación.
- [x] Escribir el [estándar de documentación](../../referencia/estandar-documentacion.md).
- [x] Crear las plantillas de ticket, cambio, ADR y postmortem ([ver](../../referencia/plantillas.md)).
- [x] Script de saneo de secretos (`scripts/sanear_configs.py`) y verificación automática en el CI.
- [x] Publicar el sitio en GitHub Pages.
- [x] Crear el sitio de Jira Service Management (`lupulo-litoral.atlassian.net`, proyecto `LL`).
- [x] Configurar Jira: tipos de solicitud del portal, clientes (Martín y Sofi, organización Lúpulo Litoral), resoluciones y SLA.
- [ ] Traducir al español los campos de los formularios del portal.
- [ ] Instalar Packet Tracer y comprobar que tenga WLC, teléfonos IP y dispositivos IoT.

## Misiones secundarias

- [ ] Instalar EVE-NG y levantar un FortiGate VM. Verificar qué permite la licencia de prueba (cifrado para IPsec, SD-WAN).
- [ ] Revisar si Cisco Modeling Labs Free sirve para el cap. 5 (límite de nodos, imágenes, RAM).

## Diseño y decisiones

- [ADR-001](../../decisiones/adr-001-herramienta-sitio.md): Material for MkDocs para el sitio.
- [ADR-002](../../decisiones/adr-002-gestion-tickets.md): Jira Service Management para los tickets.

### Estructura del repo

```text
lupulo-litoral-lab/
├── mkdocs.yml                 # configuración del sitio
├── requirements.txt           # versiones fijadas de MkDocs y Material
├── .github/
│   └── workflows/pages.yml    # verifica secretos, construye y publica
├── plantillas/                # ticket, cambio, ADR, postmortem
├── scripts/                   # saneo de secretos
├── privado/                   # configs crudas (ignorado por git)
└── docs/                      # todo lo que se publica
    ├── capitulos/
    │   └── capNN-nombre/
    │       ├── index.md       # historia, diseño y decisiones del capítulo
    │       ├── diagrama.drawio + diagrama.png
    │       ├── configs/       # saneadas
    │       ├── capturas/      # .pcapng y capturas comentadas
    │       └── tickets/       # LL-NN.md (informe de cada ticket de Jira)
    ├── decisiones/            # ADRs
    ├── referencia/            # estándar, mapa de cobertura, inventario, plantillas
    └── tickets/               # índice de todos los tickets
```

## Entregable

Repo listo, estándar de documentación, plantillas y tablero.

---

!!! abstract "Summary (English)"
    Chapter 0 sets up the toolkit: a public repository that doubles as a documentation site (Material for MkDocs on GitHub Pages), a documentation standard based on ITIL, NIST SP 800-61, ADRs and Diátaxis, templates for incidents, changes, ADRs and postmortems, and a script that redacts secrets from network configs before they are committed, enforced in CI.

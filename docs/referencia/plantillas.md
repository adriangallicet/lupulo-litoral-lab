# Plantillas

Para usarlas, copiá el archivo de la carpeta [`plantillas/`](https://github.com/adriangallicet/lupulo-litoral-lab/tree/main/plantillas) del repo. Escribilas como si las leyera otro técnico que tiene que retomar tu trabajo.

## Ticket de incidente

Va en `docs/capitulos/capNN-*/tickets/LL-NN.md`, con la clave del ticket de Jira.

````markdown
--8<-- "plantillas/ticket.md"
````

## Solicitud de cambio

````markdown
--8<-- "plantillas/cambio.md"
````

## ADR

Va en `docs/decisiones/adr-NNN-titulo-corto.md` y se agrega al índice de decisiones.

````markdown
--8<-- "plantillas/adr.md"
````

## Postmortem

Para incidentes graves (P1, o P2 de más de una hora). Estructura basada en NIST SP 800-61.

````markdown
--8<-- "plantillas/postmortem.md"
````

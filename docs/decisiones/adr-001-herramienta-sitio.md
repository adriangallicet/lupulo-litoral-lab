---
tags:
  - cap00
  - adr
  - documentacion
---

# ADR-001: Material for MkDocs para el sitio de documentación

| Campo | Valor |
| --- | --- |
| Fecha | 2026-11-16 |
| Estado | Aceptada |
| Capítulo | 0 |

## Contexto

El lab necesita un lugar público donde la documentación se lea bien: un portfolio para mostrar en entrevistas, no solo un repo con archivos sueltos. Requisitos:

- Que el contenido sea Markdown dentro del mismo repo que las configs (una sola fuente, versionada con git).
- Gratis, publicado en GitHub Pages.
- Búsqueda, navegación por capítulos y **etiquetas por tema**, para que "OSPF" lleve a toda la evidencia de OSPF.
- Que se lea como documentación técnica de un integrador: tablas, avisos, bloques de código con botón de copiar, diagramas Mermaid.
- Poco mantenimiento: el tiempo es para las redes, no para pelear con el sitio.

La referencia visual inicial fue [Hack Notes](https://hacknotes.github.io/), hecho con Jekyll y Minimal Mistakes.

## Decisión

Usar **Material for MkDocs** con las versiones fijadas en `requirements.txt` (`mkdocs<2`, `mkdocs-material<10`), construido y publicado por GitHub Actions.

## Alternativas descartadas

| Alternativa | Por qué no |
| --- | --- |
| Jekyll + Minimal Mistakes | Es un tema de blog: ordena por fecha. Este proyecto se lee por capítulos y por tema, no cronológicamente. Además suma Ruby a un proyecto que ya usa Python. |
| Solo READMEs en GitHub | Cero mantenimiento, pero sin búsqueda, sin etiquetas y con navegación pobre. Queda como respaldo: todo es Markdown y se lee igual en GitHub. |
| Zensical | Sucesor de Material for MkDocs hecho por el mismo equipo, que lee el mismo `mkdocs.yml`. Todavía está en versiones 0.0.x; para un proyecto de 7 a 9 meses conviene una base estable. |

## Consecuencias

- **A favor:** búsqueda en español, etiquetas, modo claro/oscuro, diagramas Mermaid y tablas sin código extra. Una sola herramienta en Python.
- **En contra:** Material for MkDocs está en modo mantenimiento desde fines de 2025 (solo correcciones críticas; las funciones nuevas van a Zensical). Con las versiones fijadas el sitio sigue compilando igual aunque no haya novedades. Fijar `mkdocs<2` es obligatorio: MkDocs 2.0 elimina el sistema de plugins y temas, y Material advierte que no es compatible.
- **Contra la estructura original de la bitácora:** MkDocs exige que el contenido publicado viva en `docs/`. Las carpetas de capítulo pasan de la raíz a `docs/capitulos/`. Las plantillas quedan en `plantillas/` y el sitio las muestra desde ahí.
- **A revisar:** cuando Zensical llegue a una versión estable, evaluar la migración (en principio, cambiar el comando de build). Se registra en un ADR nuevo que reemplace a este.

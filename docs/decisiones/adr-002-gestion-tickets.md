---
tags:
  - cap00
  - adr
  - documentacion
---

# ADR-002: GitHub Issues + Projects para gestionar tickets

| Campo | Valor |
| --- | --- |
| Fecha | 2026-11-16 |
| Estado | Propuesta (la acepta Adrián) |
| Capítulo | 0 |

## Contexto

Los tickets del lab necesitan un lugar donde se trabajen (abiertos, en curso, cerrados) además del informe final en el sitio. La vacante de referencia pide documentación en Jira.

## Decisión

GitHub Issues con etiquetas (prioridad, tipo, sede, capítulo), formularios para incidente y cambio, y un tablero de GitHub Projects con columnas *Nuevo → En diagnóstico → Resuelto → Documentado*. El número del Issue es el número del ticket.

## Alternativas descartadas

| Alternativa | Por qué no |
| --- | --- |
| Jira (plan gratuito) | Es lo que pide la vacante, pero queda separado del repo: los commits no cierran tickets solos y quien mire el portfolio necesita otra cuenta para verlo. |
| Solo archivos Markdown | Sin estados ni tablero; no practica el flujo de una mesa de ayuda. |

## Consecuencias

- Commit, Issue e informe quedan enlazados en un solo lugar público.
- La experiencia con Jira no se practica acá. Lo que se transfiere es el flujo (prioridades, estados, SLA, cierre con causa raíz), que es lo que se evalúa en una entrevista. Si hace falta mostrar Jira puntualmente, se puede replicar un capítulo en Jira Free.

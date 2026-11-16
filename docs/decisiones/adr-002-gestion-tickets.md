---
tags:
  - cap00
  - adr
  - documentacion
  - jira
---

# ADR-002: Jira Service Management para gestionar tickets

| Campo | Valor |
| --- | --- |
| Fecha | 2026-11-16 |
| Estado | Aceptada |
| Capítulo | 0 |

## Contexto

Los tickets del lab necesitan un lugar donde se trabajen (abiertos, en curso, resueltos) además del informe final en el sitio. La vacante de referencia pide documentación en Jira, y en las mesas de ayuda de integradores se usan herramientas de ticketing con portal, colas, prioridades y SLA. Practicar con una de ellas es parte del objetivo del lab, no un detalle.

La primera propuesta fue GitHub Issues + Projects. Se descartó por la razón de arriba.

## Decisión

**Jira Service Management, plan gratuito** (hasta 3 agentes), en un sitio propio de Atlassian, con un proyecto de servicio de clave `LL`.

- Los personajes (Martín, Sofi, Lucas, Carla) reportan como *clientes* por el portal; Adrián atiende como *agente*.
- Tipos de solicitud: incidente, problema, cambio y consulta. Si el plan gratuito no incluye algún tipo de trabajo de ITSM (por ejemplo, la gestión de cambios), se crea como tipo de solicitud común y se sigue el mismo flujo con la [plantilla de cambio](../referencia/plantillas.md#solicitud-de-cambio).
- Prioridades P1 a P4 según el [estándar](../referencia/estandar-documentacion.md#7-tickets-cambios-y-jira), y SLA de primera respuesta y de resolución si el plan los ofrece.
- El ticket de Jira es el trabajo en curso; el informe `LL-NN.md` en la carpeta del capítulo es la evidencia pública. El sitio de Jira no es público, así que el portfolio se apoya en los informes.
- Integración opcional con la app *GitHub for Jira*: los commits que mencionan `LL-NN` aparecen en el ticket.

## Alternativas descartadas

| Alternativa | Por qué no |
| --- | --- |
| GitHub Issues + Projects | Todo queda en un solo lugar público y enlazado, pero no practica la herramienta que pide el mercado. |
| Jira Software (no Service Management) | Está pensado para equipos de desarrollo: sin portal de clientes ni SLA. Una mesa de ayuda N2 se parece más a Service Management. |
| GLPI (open source, en Docker) | Muy usado en mesas de ayuda de la región y combina tickets con inventario. Queda como alternativa para el cap. 7 (inventario / CMDB), pero no es lo que nombra la vacante. |

## Consecuencias

- Se practica el flujo real de una mesa de ayuda: portal, colas, prioridades, SLA y cierre con causa raíz.
- Hay dos lugares: Jira (trabajo) y el repo (informe). La regla para que no diverjan: un ticket no se cierra en Jira hasta que su informe está en el repo.
- Depende de las condiciones del plan gratuito de Atlassian. Si cambian, este ADR se reemplaza.

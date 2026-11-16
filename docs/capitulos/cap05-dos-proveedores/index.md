---
tags:
  - cap05
  - bgp
  - route-maps
  - sd-wan
  - redundancia-wan
  - postmortem
---

# 5. Dos proveedores

!!! note "Estado: pendiente · Plataforma: EVE-NG"
    Esta página muestra el plan. Se completa con el diseño, las decisiones y los tickets a medida que avanza el capítulo.

## El llamado

Un sábado a la noche se corta internet en la planta durante cuatro horas. Los tres bares no pueden cobrar con tarjeta porque el sistema de ventas está en la planta. Sofi llama el domingo temprano: "Esto no puede volver a pasar. Contratemos lo que haga falta".

## Núcleo

- [ ] Postmortem del corte de cuatro horas.
- [ ] Doble salida a internet con rutas estáticas flotantes y monitoreo del enlace; medir el tiempo de conmutación.
- [ ] BGP con ambos ISP, anunciando un prefijo propio simulado.
- [ ] Route-maps: local preference para la salida y AS-path prepend para la entrada.
- [ ] SD-WAN en el FortiGate con chequeos de SLA y reglas para el tráfico de ventas.

## Misiones secundarias

- [ ] Simular degradación (latencia, pérdida), no solo corte, y ver si SD-WAN reacciona.

## Diseño y decisiones

*Pendiente.*

## Tickets

*Se agregan al cerrarlos.*

## Entregable

Postmortem, informe para Sofi de "qué pasa si se corta internet" con tiempos medidos, configs BGP y SD-WAN, tickets.

## Conecta con

BGP, route-maps y SD-WAN de la vacante (fuera del temario CCNA). Es el capítulo más N3.

---

!!! abstract "Summary (English)"
    *Pending.*

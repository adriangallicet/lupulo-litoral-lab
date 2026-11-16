---
tags:
  - cap01
  - ccna2
  - ssh
  - dhcp
  - nat
  - ipv6
  - rutas-estaticas
  - cdp-lldp
---

# 1. El garage

!!! note "Estado: pendiente · Plataforma: Packet Tracer"
    Esta página muestra el plan. Se completa con el diseño, las decisiones y los tickets a medida que avanza el capítulo.

## El llamado

Martín aprobó la minuta de visita. Pide ordenar el garage: que todo tenga internet de forma estable, que la impresora no "desaparezca" y que nadie de afuera pueda entrar al router. Presupuesto chico: compran un router Cisco usado y un switch administrable.

## Núcleo

- [ ] Hostname, `enable secret`, usuario local y SSH v2; deshabilitar telnet.
- [ ] Pool DHCP en el router, excluyendo las IPs fijas.
- [ ] NAT overload hacia el ISP y ruta por defecto.
- [ ] Dual-stack: IPv6 en la LAN con SLAAC y ruta por defecto IPv6 hacia el ISP.
- [ ] Wi-Fi con WPA2 (o WPA3 si Packet Tracer lo permite) y contraseña que no sea la de fábrica.
- [ ] Relevamiento con CDP/LLDP: documentar qué ve cada equipo.
- [ ] Verificar con `ping`, `show ip nat translations`, `show ip dhcp binding` y `show ipv6 interface brief`.
- [ ] Guardar configs, sanearlas y exportarlas al repo.

## Misiones secundarias

- [ ] DHCPv6 stateless en lugar de SLAAC puro, y comparar.
- [ ] Presupuesto real con precios de MercadoLibre para el router y el switch.

## Diseño y decisiones

*Pendiente.*

## Tickets

*Se agregan al cerrarlos.*

## Entregable

Diagrama, tabla de direccionamiento (IPv4 e IPv6), configs, presupuesto y tres tickets resueltos.

## Conecta con

CCNA2 (configuración básica, DHCP, IPv6, rutas estáticas) y el requisito de DNS/DHCP de la vacante.

---

!!! abstract "Summary (English)"
    *Pending.*

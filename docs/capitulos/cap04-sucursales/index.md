---
tags:
  - cap04
  - ccna3
  - ospf
  - ipsec
  - vpn
  - fortigate
  - pfsense
  - vyos
  - monitoreo
---

# 4. Las sucursales

!!! note "Estado: pendiente · Plataforma: EVE-NG"
    Esta página muestra el plan. Se completa con el diseño, las decisiones y los tickets a medida que avanza el capítulo.

## El llamado

El taproom funciona tan bien que abren dos bares más: Gualeguaychú y Paraná. Sofi necesita que las cajas de los tres bares lleguen al sistema de ventas de la planta, y Martín quiere ver las cámaras de todos lados. "¿Hay que tirar un cable hasta Paraná?". No: internet con túneles cifrados.

## Núcleo

- [ ] Primero, rutas estáticas entre sedes, y por qué no escalan.
- [ ] OSPF en la planta y entre routers de sucursal.
- [ ] VPN IPsec site-to-site FortiGate ↔ pfSense y FortiGate ↔ VyOS, con tabla de parámetros de fase 1 y fase 2.
- [ ] Políticas en el FortiGate: cajas solo al servidor de ventas; cámaras solo al grabador.
- [ ] Zabbix básico: disponibilidad por ping y SNMP de las tres sedes.
- [ ] Capturas con Wireshark de la negociación IKE y de la formación de adyacencias OSPF.

## Misiones secundarias

- [ ] El bar heredado: integrar una red con EIGRP al OSPF de la empresa con redistribución.
- [ ] Formación gratuita de Fortinet (nivel inicial).

## Diseño y decisiones

*Pendiente.*

## Tickets

*Se agregan al cerrarlos.*

## Entregable

Diagrama WAN, tabla de parámetros VPN, capturas comentadas y tickets.

## Conecta con

CCNA3 (OSPF, VPN, NAT, gestión de red) y VPN, L2L, routing dinámico y firewalls multivendor de la vacante.

---

!!! abstract "Summary (English)"
    *Pending.*

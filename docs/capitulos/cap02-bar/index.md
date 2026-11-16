---
tags:
  - cap02
  - ccna2
  - vlan
  - inter-vlan
  - wireless
  - port-security
  - dhcp-snooping
  - dai
  - acl
---

# 2. El primer bar

!!! note "Estado: pendiente · Plataforma: Packet Tracer"
    Esta página muestra el plan. Se completa con el diseño, las decisiones y los tickets a medida que avanza el capítulo.

## El llamado

Abren un taproom al lado del garage: dos cajas con posnet, cámaras de seguridad, una PC de administración, un teléfono IP para tomar pedidos y Wi-Fi para los clientes. Sofi tiene una sola preocupación: "Que ningún cliente desde el Wi-Fi pueda ver nada nuestro". Martín agrega: "Y que si algo falla, sepamos dónde".

## Núcleo

- [ ] VLANs y puertos de acceso; trunk entre switch y router.
- [ ] Primera versión con router-on-a-stick (subinterfaces).
- [ ] Migración a switch L3 (3650) con SVI e `ip routing`, documentada en un ADR.
- [ ] DHCP por VLAN (en el L3 o con `ip helper-address`).
- [ ] Voice VLAN en el puerto del teléfono IP.
- [ ] Wi-Fi con WLC y AP lightweight: SSID para clientes mapeado a su VLAN.
- [ ] ACLs: WIFI-CLIENTES solo sale a internet; CAMARAS solo habla con ADMIN; GESTION solo accesible desde ADMIN.
- [ ] Seguridad de LAN: port security en puertos de cajas, DHCP snooping y DAI.
- [ ] VLAN nativa distinta de 1 y puertos sin usar apagados en una VLAN "parking".

## Misiones secundarias

- [ ] SSID corporativo separado para el personal, con su propia VLAN.
- [ ] Matriz de flujos exportada como tabla de referencia reutilizable.

## Diseño y decisiones

*Pendiente.*

## Tickets

*Se agregan al cerrarlos.*

## Entregable

Diseño AS-IS (garage) y TO-BE (bar), tabla de VLANs, matriz de qué VLAN puede hablar con cuál, configs, ADR de la migración y tickets.

## Conecta con

CCNA2 (VLANs, inter-VLAN, seguridad de LAN, WLAN), la práctica en MSI (Stratix, SVI, ACL de mínimo privilegio) y VLANs, wireless y seguridad de la vacante.

---

!!! abstract "Summary (English)"
    *Pending.*

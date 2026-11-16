---
tags:
  - cap03
  - ccna2
  - stp
  - etherchannel
  - hsrp
  - acl
  - ot
  - iot
---

# 3. La planta

!!! note "Estado: pendiente · Plataforma: Packet Tracer"
    Esta página muestra el plan. Se completa con el diseño, las decisiones y los tickets a medida que avanza el capítulo.

## El llamado

El garage quedó chico. Alquilan una nave en el parque industrial y compran seis tanques de fermentación. Martín quiere ver temperatura y presión de cada tanque desde el celular, con sensores ESP32 que publican por MQTT. Contratan a Lucas para mantenimiento. A la semana, Lucas conecta un switch de oficina "para tener más bocas" y se cae toda la red de la planta. Martín llama nervioso: "Si la temperatura de un tanque se dispara y no nos enteramos, perdemos 2.000 litros".

## Núcleo

- [ ] Zonas IT, OT y DMZ, con modelo Purdue simplificado y vocabulario de zonas y conductos de IEC 62443.
- [ ] Dos switches de distribución redundantes y switches de acceso con doble enlace.
- [ ] HSRP entre los switches de distribución.
- [ ] Spanning tree: root bridge elegido a propósito (alineado con el HSRP activo), Rapid PVST+, PortFast y BPDU Guard en puertos de usuario.
- [ ] EtherChannel (LACP) entre los switches de distribución.
- [ ] Port security en los puertos del panel y de los sensores.
- [ ] ACL que permita solo lo necesario entre IT y OT.
- [ ] Línea base de comunicaciones esperadas de la zona OT.

## Misiones secundarias

- [ ] Radioenlace al depósito a 3 km: presupuesto de enlace, zona de Fresnel, equipos y costo.
- [ ] Root guard en los puertos hacia el acceso y comparación con BPDU Guard.

## Diseño y decisiones

*Pendiente.*

## Tickets

*Se agregan al cerrarlos.*

## Entregable

Diagrama por zonas, matriz de flujos IT-OT, documento corto de "por qué segmentamos" para Martín (sin jerga) y tickets.

## Conecta con

CCNA2 (STP, EtherChannel, FHRP, seguridad de LAN), spanning tree de la vacante, la experiencia OT en MSI y la tesis IoT.

---

!!! abstract "Summary (English)"
    *Pending.*

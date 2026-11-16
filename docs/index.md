---
hide:
  - navigation
---

# Lúpulo Litoral

**Un home-lab de redes contado como una historia.** Lúpulo Litoral es una cervecería artesanal ficticia que arranca en un garage de Concepción del Uruguay y crece hasta ser una empresa con planta, bares y clientes grandes. Yo soy su consultor de redes: cada capítulo es un pedido del cliente que resuelvo en el lab, documento y defiendo como si fuera un trabajo real.

La empresa es inventada. Las configuraciones, las fallas, los diagnósticos y las decisiones son reales.

<div class="grid cards" markdown>

-   :material-book-open-variant: **La historia**

    ---

    Quiénes son Martín, Sofi, Lucas y Carla, y cómo empezó todo.

    [:octicons-arrow-right-24: Leer el prólogo](historia.md)

-   :material-lan: **Capítulos**

    ---

    Del garage con un router de proveedor a una empresa con BGP, SD-WAN y guardias.

    [:octicons-arrow-right-24: Ver capítulos](capitulos/index.md)

-   :material-ticket-confirmation: **Tickets**

    ---

    Fallas diagnosticadas como soporte N2: síntoma, diagnóstico, causa raíz y solución.

    [:octicons-arrow-right-24: Ver tickets](tickets/index.md)

-   :material-tag-multiple: **Por tema**

    ---

    Toda la evidencia agrupada por tecnología: VLAN, OSPF, IPsec, STP…

    [:octicons-arrow-right-24: Ver etiquetas](etiquetas.md)

</div>

## Estado del proyecto

| Capítulo | Temas principales | Plataforma | Estado |
| --- | --- | --- | --- |
| [0. Preparación](capitulos/cap00-preparacion/index.md) | Repo, estándar, plantillas, tablero | — | :material-progress-wrench: En curso |
| [1. El garage](capitulos/cap01-garage/index.md) | SSH, DHCP, NAT, IPv6, rutas estáticas | Packet Tracer | Pendiente |
| [2. El primer bar](capitulos/cap02-bar/index.md) | VLAN, inter-VLAN, WLC, seguridad de LAN, ACL | Packet Tracer | Pendiente |
| [3. La planta](capitulos/cap03-planta/index.md) | IT/OT, STP, EtherChannel, HSRP | Packet Tracer | Pendiente |
| [4. Las sucursales](capitulos/cap04-sucursales/index.md) | OSPF, VPN IPsec multivendor | EVE-NG | Pendiente |
| [5. Dos proveedores](capitulos/cap05-dos-proveedores/index.md) | BGP, route-maps, SD-WAN | EVE-NG | Pendiente |
| [6. Nos auditan](capitulos/cap06-auditoria/index.md) | TACACS+, syslog, NTP, hardening | EVE-NG | Pendiente |
| [7. Ya somos empresa](capitulos/cap07-empresa/index.md) | Monitoreo, automatización, guardias | EVE-NG | Pendiente |

---

!!! abstract "Summary (English)"
    Lúpulo Litoral is a hands-on networking home-lab framed as a story: a fictional craft brewery grows from a garage into a multi-site company, and I am its network consultant. Each chapter is a customer request solved in Packet Tracer or EVE-NG and documented like real work: design decisions (ADRs), sanitized configs, packet captures, and troubleshooting tickets. It covers the CCNA syllabus and goes beyond it into multivendor VPNs, BGP, SD-WAN, AAA and monitoring.

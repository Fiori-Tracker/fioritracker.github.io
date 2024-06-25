---
description: 'Fiori Tracker offers flexible installation options for SAP landscapes. Follow component-specific guides.'
---

# Installation for FT Roles

In the {% if  prod.ro.cen == 'X' %} Central system {% endif %} {% if  prod.ro.man == 'X' %} Managed system
{% endif %} please execute the following steps:

1. [Obtain the and import](../../inst/step-1.md) transport files
2. [Activate Frontend ICF node](../../inst/step-2.md) for node `zftroles`
3. [Enable backend odata service](../../inst/step-3.md) for service `ZNYPERO_SRV`
4. [Assign pfcg roles](../../inst/step-4.md) for role `ZNYPE_ROMAN`


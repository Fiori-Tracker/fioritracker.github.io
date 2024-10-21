---
description: 'Fiori Tracker offers flexible installation options for SAP landscapes. Follow component-specific guides.'
---
# Installation for Fiori Tracker Core

Execute the following steps in the {% if  prod.core.cen == 'X' %} Central system: {% endif %} {% if  prod.core.man == 'X' %} Managed system: {% endif %}


1. [Obtain the and import](../../inst/step-1.md) transports files
2. [Activate Frontend ICF nodes](../../inst/step-2.md) for nodes `zftapps` and `zftcats`
3. [Enable backend odata service](../../inst/step-3.md) for service `ZNYPECOR_SRV`
4. [Assign pfcg roles](../../inst/step-4.md) for role `ZNYPE_FTMAN` and `ZNYPE_FTMEM`

If you are installing the components in the system that had their previous versions, please perform [Fiori launchpad cache reset](../../inst/flpcache.md) for the bsp applications: `zftapps` and `zftcats.`

If you are installing Fiori Tracker Core for the first time please check [Evaluation deployment](eval-dep.md) for details on installing Fiori Tracker Core to one system (f.e. Sandbox).

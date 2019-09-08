# Installation for Fiori Tracker Core

Execute the following steps in the {% if  prod.core.cen == 'X' %} Central system: {% endif %} {% if  prod.core.man == 'X' %} Managed system: {% endif %}


1. [Download and import transports](../../inst/step-1.md) from Product release page [http://get.fioritracker.org](http://get.fioritracker.org) Release `2020SPS03`
2. [Activate Frontend ICF nodes](../../inst/step-2.md) for nodes `zftapps` and `zftcats`
3. [Enable backend odata service](../../inst/step-3.md) for service `ZNYPECOR_SRV`
4. [Assign pfcg roles](../../inst/step-4.md) for role `ZNYPE_FT`

If you are installing the components in the system that had their previous versions, please perform [Fiori launchpad cache reset](../../inst/flpcache.md) for the bsp applications: `zftapps` and `zftcats.`

If you are installing Fiori Tracker Core for the first time please check [Evaluation deployment](eval-dep.md) for details on installing Fiori Tracker Core to one system (f.e. Sandbox).


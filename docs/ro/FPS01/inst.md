# Installation for FT Roles

In the {% if  prod.ro.cen == 'X' %} Central system {% endif %} {% if  prod.ro.man == 'X' %} Managed system
{% endif %} please execute the following steps:

1. [Download and import transports](../../inst/step-1.md) from Product release page [Product release page](https://github.com/fioritracker/ro/releases) Release `2020FPS01`
2. [Activate Frontend ICF node](../../inst/step-2.md) for node `zftroles`
3. [Enable backend odata service](../../inst/step-3.md) for service `ZNYPERO_SRV`
4. [Assign pfcg roles](../../inst/step-4.md) for role `ZNYPE_RO`

See also [an optional step](inst-opt.md) for installing FT Roles - Applications and Catalogs Relation: Roles.
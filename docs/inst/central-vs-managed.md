---
nype_config:
  container_css: content-only justify wide-content
---

# Central system vs. Managed system breakdown

## Products with Central and Managed components

| Product  |Component                                             | Placement         | Front-end nodes      | Odata service | Authorization role | Description  | 
| -- |-------------------------------------------------------|-------------------|----------------------|---------------|--------------------|-----|
| [{{ product.fau.name }}](https://help.fioriappsusage.org) | {{ comp.fam.name }} | Central system | {{comp.fam.fnode}} | {{comp.fam.odata}} | {{comp.fam.ro}} | {{comp.fam.desc}} |
|                                                       | {{ comp.fap.name }} | Managed system | {{comp.fap.fnode}} | {{comp.fap.odata}} | {{comp.fap.ro}} | {{comp.fap.desc}} |
| [{{ product.asis.nameshort }}](../asis/SPS02/main.md) | {{ comp.asisCen.name }} | Central system | {{comp.asisCen.fnode}} | {{comp.asisCen.odata}} | {{comp.asisCen.ro}}| {{comp.asisCen.desc}} |
|                                                       | {{ comp.asisMan.name }} | Managed system | {{comp.asisMan.fnode}} | {{comp.asisMan.odata}} | {{comp.asisMan.ro}}| {{comp.asisMan.desc}} |


## Central only products   

| Product/Component                                          | Front-end nodes      | Odata service | Authorization role | Description    | 
|----------------------------------------------------|----------------------|---------------|-----------|---------|
| [{{ prod.core.nameshort }}](../core/SPS03/main.md)    | {{prod.core.fnode}} | {{prod.core.odata}} | {{prod.core.ro}} | {{prod.core.desc}} |
| [{{ prod.ai.name }}](../ai/FPS01/main.md)             | {{prod.ai.fnode}} | {{prod.ai.odata}}| {{prod.ai.ro}} | {{ prod.ai.desc }} |
| [{{ prod.ro.nameshort }}](../ro/FPS01/main.md)        | {{prod.ro.fnode}} | {{prod.ro.odata}}| {{prod.ro.ro}} | {{prod.ro.desc}} |
| [{{ prod.fr.name }}](https://fioriroletesting.com)        | {{prod.fr.fnode}} | {{prod.fr.odata}}| {{prod.fr.ro}} | {{prod.fr.desc}} |
| [{{ prod.tu.name }}](../sap-fiori-test-users/overview.md) | {{prod.tu.fnode}} | {{prod.tu.odata}}| {{prod.tu.ro}} | {{ prod.tu.desc }}     

# Catalog Apps Report

Application provides the list of SAP Fiori apps assigned to a catalog in the chosen system. The list is presented as a SAP Fiori Smart Table with custom sorting and Microsoft Excel file format export. 

![](res/ca.png)

### Location
Has two parts:
1. Located on Central system
2. Located on Managed system

### Available extensions
Optional extension for Catalogs app that enables view of the apps (friendly names) in relation to catalog.
[Fiori Tracker Core](ft-core.md) with [FT Catalogs Relation: Apps As-Is](/ft-cats-rel-apps-asis.md)

### Other applications that might use the product
[FT Catalogs Relation: Apps As-Is](/ft-cats-rel-apps-asis.md)

### Manual Installation 
Execute the following steps:
1. [Activate Frontend ICF nodes](/inst/step-1.md) for node `zftcatapprep`
2. [Enable backend odata service](/inst/step-2.md) for service `ZNYPECACENREP_SRV`
3. [Assign pfcg roles](/inst/step-3.md)

### Installation apps
<in preparation>

### Dependencies
Requires:  
[AsIs](asis.md)

#### Technical information

[Details](/ca-tech.md)



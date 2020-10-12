# App Catalogs Report

Application provides the list of SAP Fiori catalogs assigned to SAP Fiori app in the chosen system. The list is presented as a SAP Fiori Smart Table with custom sorting and Microsoft Excel file format export.

![](res/ac.png) 

### Location
Has two parts:
1. Located on Central system
2. Located on Managed system

### Available extensions
Optional extension that enables view of the catalogs in relation to friendly application name.
[Fiori Tracker Core](ft-core.md) with [FT Apps Relation: Catalogs, As-is](ft-apps-rel-catalogs-asis.md)

### Other applications that might use the product
[FT Apps Relation: Catalogs, As-is](ft-apps-rel-catalogs-asis.md)

### Installation
Execute the following steps:
1. [Activate Frontend ICF nodes](/inst/step-2.md) for node `zftappcatrep`
2. [Enable backend odata service](/inst/step-3.md) for service `ZNYPEACCENREP_SRV`
3. [Assign pfcg roles](/inst/step-3.md)

### Dependencies
Requires:  
[AsIs](asis.md)

#### Technical information
[Details](/ac-tech.md)



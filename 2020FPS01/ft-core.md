# Fiori Tracker Core

This is a tool for keeping a record of your SAP Fiori launchpad's scope of implementation or maintenance. 

### Key features
- Easy app identification 
- Intuitive view on application's details 
- Clarity on responsibility with unique stream ownership
- Link between apps and catalogs
- Apps and catalogs linkage to other types of information (available as extensions): roles, test users, change requests, comments, change history records, implementation and test status, actual system information values and app's usage statistics

Fiori Tracker Core contains the following applications:  
1. FT applications (with core relation: To-be catalogs) - for keeping "To-be" records of applications in scope
2. FT catalogs (with core relation: To-be apps) - for keeping "To-be" records of catalogs in scope

#### Location
Central system

#### Available extensions
Optional relations that can be installed on Fiori Tracker core
1. [FT Apps Relation: Catalogs, As-is](ft-apps-rel-catalogs-asis.md)
2. [FT Apps Relation: Apps' Usage](ft-apps-rel-appsusage.md)

#### Other applications that might use the product
1. [Fiori Apps' Usage Report](fa.md)
2. [App Catalogs Report](ac.md)

#### Installation 
[Details](/inst/ft-core.md)

#### Dependencies
Independent - does not need any other product to be installed

#### Technical information
[Details](/tech/ft-core.md) 
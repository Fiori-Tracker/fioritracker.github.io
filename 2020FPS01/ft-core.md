# Fiori Tracker Core

This product replaces multiple spreadsheets that are usually used to document SAP Fiori launchpad configuration in SAP projects.

### Key features
- Easy app identification (including documentation URLs)
- Intuitive view on application's details 
- Views dependent on application type (Fiori, SAP Gui, Custom, Extended)
- Clarity on responsibility (unique stream ownership)
- Naming conversion enforcement
- Apps and catalogs linkage to other types of information (available as extensions): roles, test users, change requests, comments, change history records, implementation and test status, actual system information values and app's usage statistics

Fiori Tracker Core contains the following Fiori Launchpad Applications:  
1. Applications (with core relation: To-be catalogs)
2. Catalogs (with core relation: To-be apps)

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
[Details](/ft-core-tech.md) 
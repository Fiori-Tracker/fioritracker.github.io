# Fiori Tracker Core

Fiori Tracker Core is a pair of apps for keeping a record of your SAP Fiori launchpad's implementation or maintenance scope. It makes a foundation for linking launchpad apps records with other project information types.

## Key features
- Easy app identification 
- Intuitive view on application's details 
- Clarity on responsibility with unique stream ownership
- Link between apps and catalogs
- Apps and catalogs linkage to other types of information (available as extensions): roles, test users, change requests, comments, change history records, implementation and test status, actual system information values and app usage statistics

Fiori Tracker Core contains the following applications: 

1. [FT applications (with core relation: To-be catalogs)](../../core/SPS02/apps.md) - for keeping ["To-be" records](../../to-be.md) of applications in scope
2. [FT catalogs (with core relation: To-be apps)](../../core/SPS02/cats.md) - for keeping ["To-be" records](../../to-be.md) records of catalogs in scope

## [Installation](inst.md)

## Location
{% if  prod.core.cen == 'X' %}
Central system
{% endif %}
{% if  prod.core.man == 'X' %}
Managed system
{% endif %}

## Available extensions
Optional relations that you can install on Fiori Tracker core

1. [FT Apps Relation: Catalogs, As-is](../../apps-rel-catalogs-asis/FPS01/main.md)
2. [FT Catalogs Relation: Apps, As-is](../../cats-rel-apps-asis/FPS01/main.md)
3. [FT Apps Relation: Apps' Usage](../../apps-rel-appsusage/FPS01/main.md) (Paid)

## Other applications that might use the product
1. [App Catalogs Report](../../ac/FPS01/main.md)
2. [Fiori Apps' Usage Report](http://help.fioriappsusage.org) (Paid)


## Dependencies
Independent - does not need any other product to be installed

## [Technical information](tech.md) 

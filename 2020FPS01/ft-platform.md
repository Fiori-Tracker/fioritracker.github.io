# Fiori Tracker family

Fiori Tracker is a family of apps for keeping a record of your SAP Fiori launchpad's implementation or maintenance scope. The scope is the list of the applications and catalogs you plan to implement or support (in Fiori Tracker apps referred as "To-be" records). Application's and catalog's "To-be" records serve as a reference for comparison with actual system configuration (in Fiori Tracker apps called "As-is"). "As-is" relations enable the project team to control setting up the SAP Fiori launchpad, crucial in projects with many applications deployed across multiple systems.

### Main apps
[Fiori Tracker Core](ft-core.md) - This kit of two apps for keeping a record of your SAP Fiori launchpad's applications and catalogs

### Optional relations for Fiori Tracker

?> Relations are optional snap-ins that you can add to Fiori Tracker Core apps to extend their functionality.  You can choose to install the relations that are only relevant to your project.

*System values relations*<br>
[FT Catalogs Relation: Apps As-is](/ft-cats-rel-apps-asis.md) - This relation shows a list of currently configured applications in the selected catalog. It enables you to view the list in each of your Managed systems.<br>
[FT Apps Relation: Catalogs, As-is](ft-apps-rel-catalogs-asis.md) - This relation shows a list of currently configured catalogs that contain the selected application. You can see the list of the catalogs in each of your Managed systems.

*Application usage relation*<br>
[FT Apps Relation: Apps' Usage](ft-apps-rel-appsusage.md) - This relation shows the list of users that started the application. The list is available for each of your Managed systems.

### Import tool
[Catalog Import](ci.md) - Lets you import your catalogs from your system into the FT catalogs list.

### Plugin for as-is information
[AsIs](asis.md) - Enables Managed system to sent the data to a Central system

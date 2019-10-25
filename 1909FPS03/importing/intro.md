## Introduction

Fiori Tracker has function to import the details of the apps that you have stored earlier in any other form. You can import your apps details using the CSV file prepared in Excel.

Function is available with: `Catalog App (Admin mode) -> Details -> Import CVS`

Additional screen before import with function to wipe the apps records before the import from CVS file. We added this function to enable repeated imports of large sets of apps data during migration to Fiori Tracker from other sources. We introduced it as you might need more than one iteration to have the correct app records in Fiori Tracker. Also implementing mass corrections and data cleaning is easier in Excel than in Fiori Tracker. 

## Apps import - using business catalog view

You can easily import applications from Business Catalogs; once you do it, Fiori Tracker automatically assigns them to the desired catalog.
Before you can start import - you have to prepare .csv, so it contains these fields:
> AppID;AppName;AppType;TechCat;SemObj;SemAct;OriginalLibraryId;OriginalAppName;AreaCode;IsLighthouse;TileTitle;FLPrunnable 

Fields' description:
- AppID - application id (f. e. from Fiori Apps Reference Library)
- AppName - application name
- AppType - application type (f.e. Standard Fiori, GUI)
- TechCat - a technical catalog
- SemObj - semantic object
- SemAct - semantic action
- OriginalLibraryID - original application id (needed for extended apps)
- OriginalAppName - original application name (needed for extended apps)
- AreaCode - code of business area (f. e. FI, SD)
- IsLighthouse - is application a lighthouse one? if yes - fill with '1', if not - fill with '0' (described here: https://help.sap.com/viewer/187a50cf8191418ab7b52505fcef1789/Ship/en-US/5120e28178954d2c919c446ed9fcb1bb.html)
- FLPrunnable - can you run the application using a Fiori Launchpad tile? if yes - fill with '1', if not - fill with '0'

> Please find an example of our input file:
 [import-example.csv](./importing/import-example.csv ':ignore')

 Then you can proceed to the desired catalog and select Import -> Applications CSV

![](/res/import_from_csv.png)

Once you select it, you can see this view. If you need you can modify here your entries and import them. 

![](/res/finalimport.png)
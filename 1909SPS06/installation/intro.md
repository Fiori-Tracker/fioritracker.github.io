# Introduction

Fiori Tracker has three parts:
1. Main Part
2. Add-on for "As-is" information
3. Plugin for application usage (optional)

To obtain the installation files see section "[Getting transports](trans)".

Part 3. "Plugin for application usage" is optional so you can skip it and the rest of the functions will work properly.

"Main Part" is composed of:
-	"Fiori Tracker" - Web browser run, custom SAP UI5 application run from Fiori launchpad or as standalone SAP UI5 application together with its oData services
-	“Fiori Tracker Setup” – ABAP report in the form of custom ABAP program run in SAP Gui with transaction se38

Section "[Location](deployment/location.md)" explains where in your landscape "Main part" should be installed to.

"Add-on for "As-is" information is composed of:
-   Set of ABAP function modules triggered from "Main part" 

"Plugin for application usage" is composed of:
- "Application usage plugin" - UI5 application that is loaded and run automatically as SAP Fiori launchpad plugin for all users with role ZFT_LOGGER
- OData service used by SAP Fiori launchpad plugin
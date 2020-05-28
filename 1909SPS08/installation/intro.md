# Introduction

Fiori Tracker has two parts:
1. Main Part
2. Add-on for "As-is" information (optional)

To obtain the installation files see section "[Getting transports](trans)".

"Main Part" is composed of:
-	"Fiori Tracker" - Web browser run, custom SAP UI5 application run from Fiori launchpad or as standalone SAP UI5 application together with its oData services
-	“Fiori Tracker Setup” – ABAP report in the form of custom ABAP program run in SAP Gui with transaction se38

Section "[Location](deployment/location.md)" explains where in your landscape "Main part" should be installed to.

"Add-on for "As-is" information is composed of:
-   Set of ABAP function modules triggered from "Main part" 

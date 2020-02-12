# SapVersion

**Sets your S/4 HANA version**

Used in:
-	Generating link to Fiori library entry for an application. 
Fiori Tracker places a link for each Application Id for a standard Fiori application that has Fiori Library entry. The link is version-specific.

When set to **True** then Fiori Tracker will use a dedicated set of oData collections that authors prepared as a workaround for lack of the case insensitive queries in SAP Gateway 7.40 witch is the most popular version of SAP Solution Manager. When set to **False** Fiori Tracker will use the set of oData collection that use the standard function.
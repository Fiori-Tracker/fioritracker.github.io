---
date: 2020-02-24
slug: "SPS03/spreadsheet-challenge"
categories:
  - Project management
---
# Avoiding the pain of using spreadsheets for SAP Fiori content management

Content duplication, 1 to N mapping, and consistency

<!-- more -->

The following are the challenges that the team will face when storing scope detail in the spreadsheet.

|Challenge|Description|Fiori Tracker function|
|--|--|--|
|Duplication | Different team members can easily create duplicate records for the same content|On each record creation Fiori Tracker checks if the record already exists and does not allow creating duplicates.|
|Maintaining 1 to N mapping | It is not possible to maintain and present in an easily readable form the 1 to N relation that is needed for mapping apps to catalogs. The same applies for catalogs to roles, and roles to users mapping. |Fiori Tracker enables maintaining the mapping of an app to many catalogs and automatically updates the view showing all the apps for one catalog|
|Consistency | When adding a new app to the spreadsheet, it is relatively hard to check whether the app is already present in other catalogs. In that case, it could make sense to reuse an existing catalog. | With Fiori Tracker you can see which catalogs use the app and which one would be the best match for the role. This limits the number of catalogs and the overall complexity of Fiori launchpad configuration. |
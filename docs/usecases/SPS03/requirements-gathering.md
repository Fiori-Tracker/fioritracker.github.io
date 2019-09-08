# Fiori Launchpad Content requirements gathering

Collecting requirements in the preparation phase of SAP implementation requires teamwork. Both technical and functional experts are involved. For large projects with multiple streams, the team needs a central directory of agreed Fiori Launchpad content. Usually, the team uses a shared spreadsheet. Unfortunately, shared sheets often get out of sync, making most of the parts out of date. Once they are out of date, handling any catalog or role changes becomes a nightmare.

[![](res/sheets.png)](res/sheets.png)

 Rather than storing your Fiori launchpad content details in spreadsheets, you manage them as ["To-be" records](../../to-be.md) with a dedicated app: Fiori Tracker. 
 
 
 The application serves as a single, shared point of truth accessible to all team members, enabling simultaneous edits. The app also enables data quality control, as it limits possible entries only to the correct ones. The application also checks certain fields to prevent duplication. The check is crucial, for example, for catalogs and [Fiori app identifiers](app-identification.md). You can see how the existing apps are linked with the existing catalogs and what impact the changes will have to the catalogs. You get the view on the history of the changes. All changes [get logged with user, date, and time stamp](../../../hi/FPS01/main/).
 
## The challenges

Fiori content records (for example, apps records) kept in the spreadsheet cause many challenges. Here are the most important ones:

- Unauthorized, accidental modification causing inconsistencies
- Lack of history and origin of changes
- Duplication
- Lack of 1 to N relation maintenance

See ["The challenges of storing Fiori content records in the spreadsheet"](spreadsheet-challenges.md) for more details.





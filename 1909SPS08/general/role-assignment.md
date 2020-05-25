# Role assignment for FT apps

Below you can find all roles that provided by Fiori Tracker team and their relations to apps.
- ZFT_ALL
- ZFT_BASIS
- ZFT_FIORIDEV
- ZFT_FUNCTIONAL_APP_EXPERT
- ZFT_PMO
- ZFT_TESTER
- ZFT_SUPPORT_EXPERT

![](res/table_from_role_assignments.png)

<!---
|App                    |  ALL  |  BASIS  |  FIORIDEV  |     FUNC_APP_EXPERT     |  PMO  |  TESTER  |  SUPPORT_EXPERT  |
| : ---------------- :  | :---: | :-----: | :--------: | :---------------------: | :---: | :------: | :--------------: |
|Applications - display |   X   |    X    |            |            X            |       |     X    |         X        |       
|Applications - change  |   X   |         |     X      |                         |       |          |                  |
|Catalogs - display     |   X   |    X    |            |            X            |       |     X    |         X        |
|Catalogs - change      |   X   |         |     X      |                         |       |          |                  |
|Roles - display        |   X   |    X    |            |            X            |       |     X    |         X        |
|Roles - change         |   X   |         |     X      |                         |       |          |                  |
|App usage              |   X   |    X    |     X      |            X            |   X   |     X    |         X        |
|Missing apps           |   X   |    X    |     X      |                         |       |          |                  |
|Requests - display     |   X   |         |            |            X            |       |     X    |         X        |
|Requests - admin       |   X   |    X    |     X      |                         |       |          |                  |
|Health check           |   X   |    X    |     X      |                         |       |          |                  |
|Odata manager          |   X   |         |     X      |                         |       |          |                  |
|Fiori Tracker - setup  |   X   |    X    |            |                         |       |          |                  |
|Managed systems - setup|   X   |    X    |     X      |                         |       |          |                  |
|Info records - editor  |   X   |         |     X      |                         |       |          |                  |
--->

Roles are prepared with catalogs with separation of Target Mappings and Tiles.

The catalog with Tiles only: ZC_FT_TILES - contains all Tiles definitions for all Fiori Tracker applications.

The catalogs with Targets only: ZC_FT_BASIS, ZC_FT_FIORIDEV, ZC_FT_FUNCTIONAL_APP_EXPERT, ZC_FT_PMO, ZC_FT_TESTER, ZC_FT_SUPPORT_EXPERT contain Target definitions only for respective project roles.
# Fiori Tracker Relations

`Relations` represent the link form records for applications and catalogs to any other objects that you would like to track.

## Standard relations 
There are two standard relations that come with FT Applications and FT Catalog apps:

FT Apps Relation: [To-be Catalogs](../../core/SPS03/apps-rel-tobe-cats.md) - for keeping ["To-be"](../../to-be.md) assignments of apps to catalogs

FT Catalogs Relation: [To-be Apps](../../core/SPS03/cats-rel-tobe-apps.md) - for keeping ["To-be"](../../to-be.md) assignments of catalogs to applications 

In addition to standard relations, you can install optional ones. You choose the relations that are relevant to your project. You can also build your custom relations.

## Optional relations

### System value relations

FT Catalogs Relation: [Apps As-is](../../cats-rel-apps-asis/FPS01/main.md) - This relation shows a list of currently configured applications in the selected catalog. It enables you to view the list in each of your Managed systems.<br>

FT Apps Relation: [Catalogs, As-is](../../apps-rel-catalogs-asis/FPS01/main.md) - This relation shows a list of currently configured catalogs that contain the selected application. You can see the list of the catalogs in each of your Managed systems.

FT Apps Relation: [Apps Usage](../../apps-rel-appsusage/FPS01/main.md) (paid)
This relation shows how many times the user started the app. You can see the start count in each system configured to send the data (active Apps Usage Plugin).

FT Systems Relation: [Apps As-is](../../sys-rel-apps-asis/SPS02/main.md)
This relation shows a list of all currently configured apps in a chosen system.

FT Systems Relation: [Catalogs As-is](../../sys-rel-cats-asis/SPS02/main.md)
This relation shows a list of all currently configured catalogs in a chosen system.

### Info records relations
FT Apps and Catalogs Relation: [Change Requests](../../rel-ch/FPS01/main.md) {{ prod.RelCh.desc }}

FT Apps and Catalogs Relation: [Sign-offs](../../rel-so/FPS01/main.md) {{ prod.RelSo.desc }}

FT Apps and Catalogs Relation: [Comments](../../rel-cm/FPS01/main.md)

FT Apps and Catalogs Relation: [Test users](../../rel-tu/FPS01/main.md)

FT Apps and Catalogs Relation: [History](../../rel-hs/FPS01/main.md)

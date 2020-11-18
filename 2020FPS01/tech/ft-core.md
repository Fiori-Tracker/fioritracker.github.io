# Fiori Tracker Core - Technical Details

## Central System Components

Transport Package: ZNYPE**FT**CEN**COR**

Odata Service Name: ZNYPEFTCENCOR_SRV

#### App: "FT Applications"

Launch Path:
* https://`host:port`/sap/bc/ui5_ui5/sap/zftapps

Frontend ICF nodes
* Path:
    * default_host/sap/bc/ui5_ui5/sap/
* Node:
    * zftapps

PFCG Role: ZNYPE_FT

Fiori Launchpad Designer Settings<br>
* Catalog: ZCNYPEFT
* Group: ZGNYPEFT

Tile: "FT Core Applications"<br>
* Semantic Object: ZNYPEFTAPPS
* Action: display
* ID: nype.ft.app
* Icon: sap-icon://grid

#### App: "FT Catalogs"

Launch path:
* https://`host:port`/sap/bc/ui5_ui5/sap/zftcats

Frontend ICF nodes
* Path:
    * default_host/sap/bc/ui5_ui5/sap/
* Node:
    * zftcats

PFCG Role: ZNYPE_FT

Fiori Launchpad Designer Settings<br>
* Catalog: ZCNYPEFT
* Group: ZGNYPEFT

Tile: "FT Core Catalogs"<br>
* Semantic Object: ZNYPEFTCATS
* Action: display
* ID:  nype.ft.catalog
* Icon: sap-icon://group-2
# Fiori Tracker Core - Technical Details

## Central System Components

Transport Package: ZNYPE**FT**CEN**COR**

Odata Service Name: ZNYPEFTCENCOR_SRV

### App: "FT Applications"

Launch Path:

- https://`host:port`/sap/bc/ui5_ui5/sap/zftapps

Frontend ICF nodes

- Path:
  - default_host/sap/bc/ui5_ui5/sap/
- Node:
  - zftapps

PFCG Role: ZNYPE_FT

Fiori Launchpad Designer Settings<br>

- Catalog: ZCNYPEFT
- Group: ZGNYPEFT

Tile: "FT Core Applications"<br>

- Semantic Object: ZNYPEFTAPPS
- Action: display
- ID: nype.ft.app
- Icon: sap-icon://grid

### App: "FT Catalogs"

Launch path:

- https://`host:port`/sap/bc/ui5_ui5/sap/zftcats

Frontend ICF nodes

- Path:
  - default_host/sap/bc/ui5_ui5/sap/
- Node:
  - zftcats

PFCG Role: ZNYPE_FT

Fiori Launchpad Designer Settings<br>

- Catalog: ZCNYPEFT
- Group: ZGNYPEFT

Tile: "FT Core Catalogs"<br>

- Semantic Object: ZNYPEFTCATS
- Action: display
- ID: nype.ft.catalog
- Icon: sap-icon://group-2

# Help references

1. When library is not 1.52 at the very beginning when FT version cannot be checked yet (odata not avaialble):
   https://help.fioritracker.org/V2020/ui5lib-options
   index.html

2. If odata service is not responding:
   https://help.fioritracker.org/V{1}/inst/step-3
   {1} first part of version ("2020")
   i18n.properties

3. When library is not 1.52 and version of FT was read from odata
   https://help.fioritracker.org/V{view>/ftVersionPath}/ui5lib-options
   webapp/view/fragments/WarningPopover.fragment.xml-12

# Version fallback


# Releasing

When new release:

Change release name in

1. class version
2. Manifest .json
3. Help references

# Extending Fiori Tracker

The Fiori Tracker family lets you extend Application and Catalog functionality by building custom relations.

# Rules for building custom relations

To add a new relation you need to create an entry in table: ZFT_RELATION:
* SOURCE (Relation source)
	- Description: OData entity type name
	- Value type: Edm.String
* MAIN_OBJECT (Main object)
	- Description: Application type
	- Value type: Edm.String: 'Application' | 'Catalog'
* NAME (Relation name)
	- Description: Relation title displayed in 'Relations' list
	- Value type: Edm.String
* TYPE (Relation type)
	- Description: Relation text displayed in 'Relations' list
	- Value type: Edm.String
* SUBTYPE (Relation subtype)
	- Description: Relation subtype used for navigation purposes
	- Value type: Edm.String: 'List' | 'Sys dep List'
* LIST_POSITION (List position)
	- Description: Relation position in 'Relations' list
	- Value type: Edm.Int32

## SUBTYPE: 'List'

For each relation with 'SUBTYPE' equal to 'List' 2 collections and 2 navigation properties must be created.

### Collections

1. ${SOURCE}Set
	* Description: Collection used for display mode
	* Example:
	```
    	SOURCE: CatToBeApplication
        Collection name: CatToBeApplicationSet
    ```
1. ${SOURCE}EditSet
	* Description: Collection used for edit mode
	* Example:
	```
    	SOURCE: CatToBeApplication
        Collection name: CatToBeApplicationEditSet
    ```

### Collection properties

Each collection must contains at least 2 key properties.
${SOURCE}EditSet must contain 'Selected' property.

1. Id
	* Description: Parent collection 'Id'
	* ABAP Field: ID
	* Type: Edm.String
1. ResourceId
	* Description: Child collection 'Id'
	* ABAP Field: RESOURCE_ID
	* Type: Edm.String

1. Selected
	* Description: Property indicates whether entity is mapped to parent or is used only for displaying resouce in list
	* ABAP Field: SELECTED
	* Type: Edm.Boolean

### Navigation properties

1. ${MAIN_OBJECT}Set/${SOURCE}Set
	* Description: Navigation property used for display mode
	* Example:
	```
    	MAIN_OBJECT: Catalog
    	SOURCE: CatToBeApplication
        Navigation property name: CatToBeApplicationSet
        Url path: /sap/opu/odata/sap/ZNYPEFTCENCOR_SRV/CatalogSet('0000000001')?$expand=CatToBeApplicationSet
    ```

1. ${MAIN_OBJECT}Set/${SOURCE}EditSet
	* Description: Navigation property used for edit mode
	* Example:
	```
    	MAIN_OBJECT: Catalog
    	SOURCE: CatToBeApplication
        Navigation property name: CatToBeApplicationSet
        Url path: /sap/opu/odata/sap/ZNYPEFTCENCOR_SRV/CatalogSet('0000000001')?$expand=CatToBeApplicationEditSet
    ```
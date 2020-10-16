# AsIs

Base addon for retrieving data from Managed system and passing it to Central system.

# General technical info
[Details](/tech/asis.md)


# działanie AsIs i procesów propagowania danych?

urgens  table: ZCI_CTL
callstack: 
ZNYPECICEN->ZNYPECICEN-COPY_ASIS_CATALOGS() # move the internal table (incoming) to ZCI_CTL
ZNYPECICEN->(FM)Z_NYPECICEN_COPY_ASIS_CATALOGS 
_
ZNYPEASISCEN->ZNYPEASISCEN-COPY_ASIS_CATALOGS() # run copying asis data to plugin CATALOG IMPORT
ZNYPEASISCEN->ZNYPEASISCEN-DOWNLOAD_CATALOGS()
ZNYPEASISCEN->(FM)Z_NYPEASISCEN_DOWNLOAD_CATALOG
ZNYPEASISCEN->(FM)Z_NYPEASISCEN_DOWNLOAD_APPS
ZNYPEASISCEN->(FM)Z_NYPEASISCEN_DOWNLOAD_CTL_APP
_
ZNYPECICEN->ZNYPECICEN-DOWNLOAD_CATALOGS()
ZNYPECICEN->ZCL_ZNYPECICEN_DPC_EXT-/IWBEP/IF_MGW_APPL_SRV_RUNTIME~EXECUTE_ACTION() (edited) 



10h
urgens  taki call stack mam dla tabeli ZCI_CTL
2h
Kamil Wężniejewski  Nie dodałem jeszcze opisu do tego, jednak cała logika związana z tym jest w 2 klasach oraz 2 FM group do tych klas:
ZNYPEASISCEN (class)
ZNYPEASISCEN (FM group)
ZNYPEASISMAN (class)
ZNYPEASISMAN (FM group)
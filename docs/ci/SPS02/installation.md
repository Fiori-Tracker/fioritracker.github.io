# Catalog Import - Installation

General Basis expert steps

1. Get the transport files from Nype's representative
2. Activate Frontend ICF nodes for node `zftcatimport`
3. Enable backend odata service for service `ZNYPECICEN_SRV`
4. Assign pfcg roles for role `ZNYPE_CI`
5. Enter the activation key


As-is plugin, Basis expert steps

1. [Install As-is on Central system](orhttps://fioritracker.org/V2020/core/SPS02/main/)
2. [Install As-is on each Managed system](https://fioritracker.org/V2020/asis/FPS01/main/) 
3. Set PUBLISH parameter to 'X' in As-is API config (data is copied on Data collection requests)



# Steps for Basis Expert

## Step 1 - Import the transports

Please import the transport requests that Fiori Tracker team provides.

## Step 2 - Activate services

**2.1** Run **SICF** transaction and activate those ICF nodes:<br/>
Path: **/default_host/sap/bc/ui5_ui5/sap/**
- zfioritracker
- zfioriodatamng<br/>

Path: **/default_host/sap/opu/odata/sap/**
- ZFIORITRACKER_SRV

## Step 3 - Assign the roles

In **PFCG** transaction assign the authorization roles to the users that you want to use for starting Fiori Tracker apps:
- ZFT_ALL
- ZFT_BASIS
- ZFT_FIORIDEV
- ZFT_FUNCTIONAL_APP_EXPERT
- ZFT_PMO
- ZFT_TESTER
- ZFT_SUPPORT_EXPERT
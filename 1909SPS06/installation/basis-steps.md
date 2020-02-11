# Steps by Basis Expert

The following steps should be executed by a Basis Expert responsible for the system tha Fiori Tracker is installed to.

## Step 1 - Import the transports

Please import the transport requests that the Fiori Tracker team provides as:
- "Central system -> Main part"
- "Central system -> Roles for Main part"

## Step 2 - Generate runtime objects for the ZFIORITRACKER_SRV service

2.1 Proceed to `SEGW` transaction. <br>a
2.2 Open project `ZFIORITRACKER`

![](res/segw.png)

2.3 Go to change mode and Generate Runtime objects for `ZFIORITRACKER_SRV` service

![](res/segw_gen.png)

## Step 3 - Add the ZFIORITRACKER_SRV service

3.1 Proceed to `/n/IWFND/MAINT_SERVICE` transaction.<br>

**If you can find `ZFIORITRACKER_SRV` entry - proceed directly to the step 4**

3.2 Click on the `Add service` button.

![](/res/maint_service_add.png)

3.3 Provide System Alias: `LOCAL` and External Service Name: `ZFIORITRACKER_SRV`.<br>
3.4 Select the record with ZFIORITRACKER_SRV and click on the `Add selected services` button.

![](/res/maint_service_add2.png)

## Step 4 - Check if ICF node status for backend service (ZFIORITRACKER_SRV) is green

4.1 Return to `/n/IWFND/MAINT_SERVICE` transaction, find and click on `ZFIORITRACKER_SRV` entry.<br>

4.2 OData status should be marked with green and there should be added `LOCAL` alias (marked as default one) - as you can see in the screenshot below.

![](/res/maint_service_status.png)

If ICF node is not marked with green then proceed with Step 5. If it is green than you can skip Step 5 and proceed with Step 6.

## Step 5 - Activate ICF node

5.1 Click on `ICF node` button and click `Activate`

![](/res/maint_service_icfactivate.png)

5.2 Then click on `SAP Gateway Client` button.

![](/res/maint_service_gwcheck.png)

5.3 Then click on the `Execute` button; you should see a HTTP response that you can see in the screenshot below.

![](/res/maint_service_httpcheck.png)

## Step 6 - Activate the Fronted ICF nodes

Run `SICF` transaction and activate those ICF nodes:<br/>
Path: `/default_host/sap/bc/ui5_ui5/sap/`
- zfioritracker<br/>
- zuideps

## Step 7 - Assign the roles

In `PFCG` transaction, assign the authorization roles to the users that you want to use for starting Fiori Tracker apps:
- ZFT_ALL
- ZFT_BASIS
- ZFT_FIORIDEV
- ZFT_FUNCTIONAL_APP_EXPERT
- ZFT_PMO
- ZFT_TESTER
- ZFT_SUPPORT_EXPERT

Role assignment for FT apps:

[Roles description](doc-cont/role-assignment.md)
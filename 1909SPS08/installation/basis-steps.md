# Steps by Basis Expert

To install Fiori Tracker, the basis expert should complete the steps described below.

## Step 1 - Import the transports

Please import the [transport requests](/trans) that the Fiori Tracker team provides as:
- "Central system -> Main part"
- "Central system -> Roles for Main part"

> Having a problem installing? Check whether this problem is a [known issue](known-issues). Also we can help. Reach out to us for installation chat support on Slack or setup a short call.

## Step 2 - Generate runtime objects for the ZFIORITRACKER_SRV service

2.1 Proceed to `SEGW` transaction. <br>a
2.2 Open project `ZFIORITRACKER`

![](res/segw.png)

2.3 Go to change mode and Generate Runtime objects for `ZFIORITRACKER_SRV` service (your user must be registered as developer)

![](res/segw_gen.png)

## Step 3 - Add the ZFIORITRACKER_SRV service

3.1 Proceed to `/n/IWFND/MAINT_SERVICE` transaction.<br>

3.2 Check for entry called: `ZFIORITRACKER_SRV`:

![](/res/maint-service-entry.png)

If the entry is present then proceed directly to the [step 4](#step-4-check-if-icf-node-is-active).

3.3 Click on the `Add service` button.

![](/res/maint-service-add.png)

3.4 Provide System Alias: `LOCAL` and External Service Name: `ZFIORITRACKER_SRV`.<br>
3.5 Select the record with ZFIORITRACKER_SRV and click on the `Add selected services` button.

![](/res/maint-service-add2.png)

## Step 4 - Check if ICF node is active

4.1 Return to `/n/IWFND/MAINT_SERVICE` transaction, find and click on `ZFIORITRACKER_SRV` entry.<br>

4.2 OData status should be marked with green and there should be `LOCAL` alias added and marked as default one. The screen should look like below:

![](/res/maint-service.png)

If ICF note is green then proceed to the [step 6](#step-6-activate-the-fronted-icf-nodes) (skip step 5).

## Step 5 - Activate ICF node

5.1 Click on `ICF node` button and click `Activate`

![](/res/maint-service-icf.png)

5.2 Then click on `SAP Gateway Client` button.

![](/res/maint-service-gw.png)

5.3 Then click on the `Execute` button; you should see a HTTP response that you can see in the screenshot below.

![](/res/maint-service-http.png)

## Step 6 - Activate the Fronted ICF nodes

Run `SICF` transaction and activate those ICF nodes:<br/>
Path: `/default_host/sap/bc/ui5_ui5/sap/`
- zfioritracker<br/>
- zuideps

## Step 7 - Assign the roles

Based on [roles description](general/role-assignment.md) in transaction `PFCG` assign the authorization roles to the users that you want to use for starting Fiori Tracker apps.


# Steps by Basis Expert

Basis expert should execute the following steps:

## Step 1 - Import the transports with plug in

In each system that you plan to manage with Fiori Tracker:

Import the transport requests that the Fiori Tracker team provides as:

- "Managed systems -> 'As-is' information add-on"

## Step 2 - Prepare the RFC destinations

You will need RFC destinations for each system that you plan to manage with Fiori Tracker. Please set RFC destinations In your central system using transaction sm59. Each RFC destination should point to one of your managed systems.

The user that is set in RFC destination needs to have type SYSTEM and the following authorizations:

Authorization: S_RFC<br>
ACTVT: 16<br>
RFC_TYPE: FUGR<br>
RFC_NAME: Z_FTASIS<br>

## Step 3 - Configure managed systems

Using SAP Gui transaction `ZFTSETUP` start `8. Modify Managed systems`:

![](/res/managed-systems.png)

For each managed system defined by column `System ID` provide respective `RFC destination` defined in Step 2 above. Leave the rest of the fields. They are updated with 

## Step 4 - Check connection status

Using SAP Gui transaction `ZFTSETUP` start `9. Connection status check Modify Managed systems`:

For correctly configured systems it should show green light in column `status` as shown on below screenshot:

![](/res/connection-status.png)

See also: [Deployment options](/deployment/intro)



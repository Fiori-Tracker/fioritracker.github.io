# Steps by Basis Expert

Basis expert should execute the following steps:

## Step 1 - Import the transports with plug in

In each system that you plan to manage with Fiori Tracker:

Import the transport requests that the Fiori Tracker team provides as:

- "Managed systems -> 'As-is' information add-on"

## Step 2 - Prepare the RFC destinations

You will need RFC destinations for each system that you plan to manage with Fiori Tracker. Please set RFC destinations In your central system using transaction sm59. Each RFC destination should point to one of your managed systems.

The user that is set in RFC destination needs to have the following authorizations:

Authorization: S_RFC
ACTVT: 16
RFC_TYPE: FUGR
RFC_NAME: Z_FTASIS

## Step 3 - Configure managed systems list with respective RFC destinations

Using SAP Gui transaction ZFTSETUP start `8. Modify Managed systems`:

![](/res/managed-systems.png)

See also: [Deployment options](/deployment/intro)



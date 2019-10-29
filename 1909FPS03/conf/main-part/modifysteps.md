You can modify Fiori Tracker config, just proceed to `ZFTSETUP` transaction

## Step 1 - Modify area codes

In this step, you can change area codes, we have already predifined some of them (FIN, O2C, O2D).

![](/res/area_codes.png)

## Step 2 - Modify application types

In this step, you can change application types. We recommend using our proposition of them based on the SAP Fiori Apps Reference Library (please find them below).

You can find detailed description of each parameter in section [Application types](/conf/main-part/apptypes.md)

![](/res/app_types.png)

## Step 3 - Modify sign off types

In this step, you can change sign off types. They should be relevant to the steps of your development process (please find the example below).

![](/res/sign_off_types.png)

## Step 4 - Modify provisioning types

In this step, you can change provisioning types. They should be relevant to your system landscape (please find the example below).

![](/res/provisioning_types.png)

## Step 5 - Modify user to are code mappings

In this step, you can change users responsible for specific business areas f.e. stream leads.

![](/res/user_to_area.png)

## Step 6 - Modify user to type mappings

In this step, you can change users responsible for the provisioning of a specific set f.e. applications.

![](/res/user_to_type.png)

## Step 7 - Modify Manged systems

In this step, you can provide connection data for your managed systems by setting:
- System ID -  SIDs of your managed systems where 'As is' addon and Application usage plugin are installed
- RFC address – name of RFC connection from your Central system to the Managed system
- Is production - enable this checkbox for your production system entry

![](/res/modify_managed_systems.png)

## Step 8 - Connection status check for Managed systems

In this step, you can check connection between your Central system and plugins/addons on your Managed systems.

![](/res/connection_check.png)
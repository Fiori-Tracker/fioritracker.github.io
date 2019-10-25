# Steps to be performed by Basis Expert

## Step 1 - Import the transport

Please import the transport requests that the Fiori Tracker team provides as:

- "Managed systems -> Applications usage plugin"
- "Managed systems -> Role for application usage plugin"

## Step 2 - Enable users to access plugin

In `PFCG` transaction assign the authorization role `ZFT_LOGGER` to the users that you want to track their applications usage data.

## Step 3 - Define RFC destination of a Central system

If you have a RFC pointing to the Central system just use it in the next step. If you do not have such RFC destination, plese prepare it in transaction `SM59`.

Run `SM30` transaction and add an entry to `ZFSL_SYST_CONFIG` table.


|  Config key   |      Config value                            |
| ------------- |:-------------------------------------------: |
|  TARGET_RFC   | `<RFC destination of your Central system>`   |

!> RFC destination user must have authorizations to run function module: Z_FT_LOG_APPLICATION_USAGE

![](/res/rfc_conf.png)

## Step 4 - Activate ICF nodes

Run transaction `SICF` and activate the following ICF nodes:

Path: `/default_host/sap/bc/ui5_ui5/sap/`:
- zfioristatslog

Path: `/default_host/sap/opu/odata/sap/`:
- zfioristatslog_srv

![](/res/sicf.png)

## Step 5 - Add system alias

Run `/iwfnd/maint_service` and add the system alias to `ZFIORISTATSLOG_SRV`.

![](/res/alias.png)

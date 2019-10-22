# Plugin for application usage

**1.** Import the transport requests for "Plugin for application usage".

**2.** In **PFCG** transaction assign the authorization role to the users that you want to track their applications usage data with Most Frequently Used Apps plugin:
- ZFT_LOGGER

**3.** Run **SM30** transaction (Gateway) and add an entry to **ZFSL_SYST_CONFIG** table.


|  Config key   |      Config value      |
| ------------- |:-------------:         |
|  TARGET_RFC   | **YOUR RFC TO SOLMAN** |

!> RFC destination user must have access to function module: Z_FT_LOG_APPLICATION_USAGE

![](../res/rfc_conf.png)

**4.** Run SICF transaction and activate those ICF nodes:

Path: /default_host/sap/bc/ui5_ui5/sap/:
- zfioristatslog

Path: /default_host/sap/opu/odata/sap/:
- zfioristatslog_srv

![](../res/sicf.png)

**5.** Run **/iwfnd/maint_service** and add the system alias to **ZFIORISTATSLOG_SRV**.

![](../res/alias.png)

# Fiori App Usage Report configuration (Central system)

To change Central part configuration start the transaction `ZFACENADMIN` and press button labeled: **2. Edit configuration**. This action will open a configuration screen:

[![](res/fiori-app-usage-report-config.png)](res/fiori-app-usage-report-config.png)

The table below describes all available parameters:

| Key                   | Value     | Description            |
|-----------------------|-----------|------------------------|
| ACTIVATION_KEY        | *key*     | Value is provided by Nype team         |
| INCOMP_HIDE           | **TRUE** | When set to TRUE the version compatibility warning will not show |
| LOGMODE               | **FULL** | Plugin will write down usage records only when this parameter is set to **FULL**. Delete this parameter to stop writing usage records. This allows stopping log collection without removing user's Fiori App Usage role.|


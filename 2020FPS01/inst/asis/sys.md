# Step 1 - Configure managed systems

1. Using SAP Gui `Admin transaction` start step `1. Modify Managed systems`:

![](inst/asis/res/managed-systems.png)

For each managed system defined by column `System ID` provide respective `RFC destination` (see [how to prepare it](/inst-ux/rfc.md). Leave the rest of the fields - they are updated automatically on *Connection status check*.

2. Check connection status

Using same SAP Gui `Admin transaction` start step `2. Connection status check Modify Managed systems`:

For correctly configured systems it should show green light in column `status` as shown on below screenshot:

![](inst/asis/res/connection-status.png)

# Step 1 - Configure managed systems

1. Using SAP Gui transaction `ZFTSETUP` start `8. Modify Managed systems`:

![](/res/managed-systems.png)

For each managed system defined by column `System ID` provide respective `RFC destination` (see [how to prepare it](rfc.md). Leave the rest of the fields - they are updated automatically on *Connection status check*.

2. Check connection status

Using SAP Gui transaction `ZFTSETUP` start `9. Connection status check Modify Managed systems`:

For correctly configured systems it should show green light in column `status` as shown on below screenshot:

![](/res/connection-status.png)

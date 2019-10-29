# Steps for UX Lead (Fiori Developer)

There are only two steps that you need to complete to setup Fiori Tracker. Find them in section `Installation` after starting transaction `ZFTSETUP` in SAP Gui:

![](res/zftsetup-inst.png)

## Step 1 - Create number range intervals

1. Choose `1. Create number range intervals`.<br />
2. Check if you got the following screen:<br />

![](res/intervals.png)

3. If yes, then you have created intervals successfully

## Step 2 - Create default initial data

1. Chose `2. Crate default initial data`
2. Check if you got the following screen:

![](res/initial.png)

3. If yes, then you have created intervals successfully. 

If yes, then you have created intervals successfully. You can adjust the initial settings later, as described in the [configuration section](/conf/main-part/conf.md). 

## Step 4 - Check if the Fiori Tracker applications run correctly

1. There are two ways to start Fiori Tracker applications:

From your SAP Fiori Launchpad:
- Login and start the SAP Fiori Launchpad with the user that you have configured in Step 3 of the installation guide.

![](res/ft_flp.png)

2. You can also start the Fiori Tracker as an standalone application by opening the following address in your browser:
- **yourhost:port**/sap/bc/ui5_ui5/sap/zfioritracker/</br>
f.e. https://demo.fioritracker.org/sap/bc/ui5_ui5/sap/zfioritracker/

![](res/ft_standalone.png)
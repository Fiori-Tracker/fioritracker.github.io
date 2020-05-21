# Known issues

There are some known issues with the installation that Fiori Tracker team is working on fixing. To see if there's a workaround for your problem, check this section.

###1 Issues for systems with SAP GateWay in version 7.40

Problem: 

When importing the main-part transports you will get return code 8 (error) as the transports were exported form system with version 7.52.
The error message you will see is: 

`The installed release does not match`.

Solution:

During transport in the pop up windows with options for transport please mark 'Ignore invalid Component version' checkbox and go ahead with this option.

LAter when continuing with imports for Main part you will get another error:

`Program ZCL_ZFIORITRACKER_DPC=========CP, Include ZCL_ZFIORITRACKER_DPC=========CM06L: Syntax error in line 000002`
`Method 'EXECUTE_ACTION' is unknown or PROTECTED or PRIVATE'`






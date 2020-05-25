# Fiori Reporter - support ticket in 6 seconds

The Reporter starts with the button placed in the Fiori launchpad top bar (available for each app). It opens a dialog, prefilled with the system id, app name, and allowing to enter short issue description. 

By marking the checkbox, you can decide if the Reporter should automatically take and attach the screenshot (no external tool is needed). 

At dialog closure, the Reporter connects to your issue tracking system (f.e. Jira) and creates the issue putting all the details:
Application ID and official name
Screenshot (as an attachment)
SU53 - missing authorizations report (as an attachment)
Frontend and backend system id, mandant, logon language
User details with the timestamp
Link to start the app

The reported issue is auto-assigned to responsible leads based on the app’s Area designation.

![](/res/fiori-reporter.gif)



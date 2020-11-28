# Location of Central system: S/4 HANA QAS or outside your system landscape?

You can install Fiori Tracker Central system components on any SAP Gateway.

Three of the most popular deployment options are described in [Deployment section](/deployment/intro.md)

Some considerations to be taken into account:

1. As Fiori Tracker becomes a repository of the vital documentation of your setup you are going to need it the most at times when your SAP Gateway systems undergo the changes and could be offline or inaccessible. For example, during upgrades or issues with Fiori content. In this case it is worth to consider to locate Fiori Tracker outside of the landscape, for example on SAP GRC system. SAP Solution Manager would be a good option only if it is upgraded at least to 7.5. Unfortunately last version of SAP Solution Manager 7.2 is based on Net Weaver 7.40 with extended support till 2027 and 7.40 is below minimal requirements that Fiori Tracker has.

2. Many Fiori Tracker users chose to use it during the preparation phase when your S/4 HANA landscape is not yet installed.

3. Main Fiori Tracker users are the members of project team. In some cases, not all project team members have users in S/4 HANA landscape but they might have in the system outside the landscape (f.e. on SAP GRC).

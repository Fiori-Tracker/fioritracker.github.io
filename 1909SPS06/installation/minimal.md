# Minimal installation requirements

**Minimal requirement is any SAP system with SAP Gateway (software component SAP_GWFND). Fiori Tracker will work in both: HUB and Embedded deployment.**

We built it on SAP Gateway, so it is not affected by the backend system version (can work both with SAP S/4 HANA and SAP Business Suite.)

Compatible systems versions with verified Fiori Tracker users include: SAP S/4 HANA 1809, 1709, 1610 (it should also work with 1503.)

Details: 

Fiori Tracker requires SAP Gateway with SAP UI5 library at least version: 1.48.9 (UI software component in version: SAP_UI 752 SP00 (or above SP)). See also,  [Deployment options](/deployment/intro.md) and [Architecture](/general/architecture.md).

For systems that do not have UI5 library in this version, Fiori Tracker can be still run from the Technical launchpad.
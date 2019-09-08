# Fiori Tracker - Frequently Asked Questions

### 1. Is it really free?

Yes, it is free for customers who agree to have their name published on the Fiori Tracker customer list. We are able to maintain Fiori Tracker with an income that [commercial pieces](com.md) of Fiori Tracker Suite provide.

### 2. Does Fiori Tracker send any data (statistics) to the outside servers (what is the security model)?

Fiori Tracker is not sending any data to outside servers. Fiori Tracker does not need external access, and many users run it on installations that do not have external access. All code is in ABAP, meaning that it is fully transparent and available for inspection.

### 3. Is Premier support mandatory after a certain time period?

No. Premier support is optional. You can continue using Fiori Tracker as it is, as long as you want, free of charge.

### 4. What are the prerequisites/minimal requirements for installation?

The minimal requirement is any SAP system with GAP Gateway (software component SAP_GWFND) on SAP NetWeaver version at least 7.52 ([see details](inst/min.md))

### 5. Will the Fiori Tracker release 2020 work on my S/4 HANA system on a different release (1610, 1709, 1809, 1909, 2021)?

Yes. Fiori Tracker release numbering is independent of SAP release numbering. Fiori Tracker release 2020 is compatible with SAP S/4 HANA releases from 1610 to 2021. Refer [Minimal requirements](inst/min.md) for more details.

### 6. What details do you need for troubleshooting the issues?

Please send the screenshots of the application running in Chrome with URL and "Developer tools" console.

Screenshot from respective SAP Gateway system from SAP Gui menu: System->Status SAP System Data -> Details.

### 7. What are the features that are available for free version (1909 SPS06) and licensed version (2020 FPS01)?

In terms of features, both versions are almost the same. The main difference is in architecture.
We have developed version 2020 FPS01 in a way that keeps Fiori Tracker Suite components independent. It is easier to support, maintain, and extend them.

If you have not found the answer to your questions in our online help, please reach out to us on Fiori Tracker Slack or [create an issue on GitHub](bugs-ideas.md).

### 8. How to de-install Fiori Tracker components?

To de-install Fiori Tracker components, please perform the reverse of the installation steps in the reverse order. For import transports steps perform the deletion of the objects from the component's transport package.

### 9. Why would I need a dedicated app instead of the shared Excel spreadsheet or Atlassian Confluence page?

App records kept in the spreadsheet cause many challenges. Here are the most important ones:

- Unauthorized, accidental modification causing inconsistencies
- Lack of history and origin of changes
- Duplication
- Lack of 1 to N relation maintenance

See ["The challenges of storing Fiori content records in the spreadsheet"](usecases/SPS03/spreadsheet-challenges.md) for more details.

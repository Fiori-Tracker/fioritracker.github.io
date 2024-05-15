# List of options for running Fiori Tracker apps on a specific UI5 library

Fiori Tracker Suite applications require access to the SAP UI5 library. They were built and tested for SAP UI5 1.52, so they work best with this specific version. They should also work with higher versions, but we have not performed the tests for them yet.

On systems with Fiori Launchpad configured the default available library will be used.

If default SAP UI5 library is not be found in your system Fiori Tracker Suite applications will automatically start using the library provided by SAP on Content Delivery Network (CDN). If the CDN is not accessible and you are not able to set UI5 library locally you can install "uideps" which will provide the library from your local system in a form of BSP. This is also the way to provide a specific version of the library for Fiori Tracker apps in case your default UI5 library version would cause issues.


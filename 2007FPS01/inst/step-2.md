# Step 2 - Enable oData service

To enable oData service complete the sub-steps described below. 

*When description refers to `Service name`, you need to put the service’s name of the run application. You can find the service’s name in the technical section of the application’s message if the service is not available.*

#### 1. Runtime objects generation in transaction SEGW

To generate objects please follow those steps:

1.1. Start transaction SEGW<br>
1.2. Using the menu Project > Open - Open project named as the first part of the `Service name`. Fe. if `Service name` is ZFIORITRACKER_SVR please open project called ZFIORITRACKER.

![](res/segw.png)

1.3. Go to Change mode and choose function Generate (you will be prompted for transport bad your user must be registered as developer)

![](res/segw_gen.png)

#### 2. Service is added to a Service Catalog

To add service please follow those steps:

2.1 Start transaction /n/IWFND/MAINT_SERVICE

2.2 Find entry with `Service name`

If the entry is present then the procedure is completed if not please execute the following sub steps:

2.3 Click on the Add service button.

2.4 Provide System Alias: LOCAL and External Service Name as the 'Service name'.

2.5 Select the record with `Service name` and click on the Add selected services button.
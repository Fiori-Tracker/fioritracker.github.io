# Fiori App Usage performance influence 

We are putting a lot of effort into making sure that the Fiori Apps usage impact on overall system performance is as low as possible. 

There is only one RFC call for each launch of the Fiori Launchpad app by the user. The code is limited to writing one entry into a transparent table. The call is made asynchronously and does not affect the start of the application.

Estimate of the space needed by records:

|Description|Measure|
|--|--|
| Each app usage record takes| 308 bytes|
| The average number of applications launches for one user in one day | 96 lauches |
| The average number of working days in the month | 20 days |
| **Space needed in a month** | **0.56 Mbytes** |
| **Space needed for 100 users in a month** | **56.4 Mbytes** |

As an extra safety measure, Fiori Apps Report has a function to stop usage recording globally without removing roles from the users. This allows turning off the logging instantly in case you have any doubts about Fiori Apps Usage’s impact on performance.

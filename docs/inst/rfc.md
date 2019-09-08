# How to prepare the RFC destinations for Managed systems

You will need RFC destinations for each system that you plan to manage with Fiori Tracker apps. Please set RFC destinations In your Central system using transaction *sm59*. Each RFC destination should point to one of your managed systems.

The user set in RFC destination needs to have type SYSTEM and the following authorizations:

Authorization object: S_RFC

|Field|Value|
|--|--|
|ACTVT| 16|
|RFC_TYPE| FUGR|
|RFC_NAME| ZNYPEASISMAN, SUNI|

|Field|Value|
|--|--|
|ACTVT| 16|
|RFC_TYPE| FUNC|
|RFC_NAME| Z_NYPEASISMAN_GET_CATALOGS, Z_NYPEASISMAN_GET_APPLICATIONS, Z_NYPEASIS_MAN_GET_VERSION, RFC_PING, FUNCTION_EXISTS|

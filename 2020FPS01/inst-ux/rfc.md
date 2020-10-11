# How to prepare the RFC destinations for Managed systems

You will need RFC destinations for each system that you plan to manage with Fiori Tracker apps. Please set RFC destinations In your Central system using transaction *sm59*. Each RFC destination should point to one of your managed systems.

The user set in RFC destination needs to have type SYSTEM and the following authorizations:

Authorization: S_RFC<br>
ACTVT: 16<br>
RFC_TYPE: FUGR<br>
RFC_NAME: Z_FTASIS<br>


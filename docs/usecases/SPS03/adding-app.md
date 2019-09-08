# Adding an application to a user

To make the application available to the user, you must first add it to the Business catalog. Then you have to assign the catalog to the role. Finally, the user must be assigned a role. 

## Challenge

The main challenge is that applications are not added directly to users. The request that might look like a quick update, might need additional decisions. Depending on the state of your current configuration adding app will require different steps. 

## How did the Fiori Tracker address the challenge?

The Fiori Tracker keeps the lists of all apps, catalogs and roles in scope. With this list, you can tell whether the new app is already in the project's scope, and drill down to learn how the team mapped the app to the catalogs and roles. If the role fits your requirement you can enable the new app by assigning the user to this role.

If the new application is not in scope already, the first step is to check in which directory and, consequently, what role you want to put the new application in. You can find a good fit by reviewing lists of apps previously assigned to the catalogs.

## Fiori launchpad content you will need to track

1. [Apps](../../tracked/SPS03/apps.md) - Fiori launchpad applications  
2. [Catalogs](../../tracked/SPS03/cats.md) - Fiori launchpad business catalogs
3. [Roles](../../tracked/SPS03/roles.md) - Authorizations roles 


## Related use cases

1. [Gathering requirements](requirements-gathering.md) - Content duplication, 1 to N mapping, and consistency   
2. [Clarity on responsibility](clarity-of-resp.md) - Diffused responsibility on the content that is shared 
2. [Naming conventions](naming.md) - Consistent naming when different team members create and change content identifiers
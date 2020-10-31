# AsIs - Development details

Base addon for retrieving data from Managed system and passing it to Central system.

### General technical info
[Details](/tech/asis.md)

### Architecture
[Details](dev/arch/asis.pptx)

`ZFT_SYSTEMS` - Main table for systems
stores general Managed system data including:
- status - when *X* means that system is available
- status_msg - 
- status_code - stable status - when *system_failure* then system needs to be updated from `ZFTASISADMINTOOL`, this is to avail long timeouts when system is not available and present an quick result for the user instead of application hanging for minutes until it fails due to timeout

Update logic:
Statuses in this table are updated only manually with report `ZNYPEASISSYSTEMSCHECK` that uses FM `Z_NYPEASIS_SYSCONNCHECK`

`ZNYPEASIS_SYS_ST` - Corresponding table for temporary use in ASIS CEN, modified only automatically (not for user):
- current status of getting the data
- last status

Statuses in this table are updated with method `znypeasiscen=>update_system_status`

Update logic:
- FM call to get the data
- if data is not returned then check what is the error with `FUNCTION_EXISTS`
- update on fields status, status_msg, module_exists
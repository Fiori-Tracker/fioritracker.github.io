# AsIs - Development details

Base addon for retrieving data from Managed system and passing it to Central system.

### General technical info
[Details](/tech/asis.md)

### Architecture
[Details](dev/arch/asis.pptx)



 `ZFT_SYSTEMS` - Main table for systems
stores general Managed system data inclding:
- status
- status_msg
- constant status (?)
Statuses in this table are updated only manually with report ZNYPEASISSYSTEMSCHECK that uses FM Z_NYPEASIS_SYSCONNCHECK

`ZNYPEASIS_SYS_ST` - Correspondig table for temporary use in ASIS CEN, modified only automatically (not for user):
- current status of getting the data
- last status


Statuses in this table are updated with method znypeasiscen=>update_system_status

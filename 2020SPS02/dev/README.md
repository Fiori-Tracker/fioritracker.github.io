# Development documentation, architecture

# General topics

### Naming conventions
1. BSP name is the same as the repo name and should comply with the following:
- short (use the )
- prefixed with "ft" (this is to avoid duplications in FT users systems , we are not using NYPE as for naming ddic objects as it too long to type in URL)

### System status logic
1. [Logic in google sheet](https://docs.google.com/spreadsheets/d/1W4Zr-m4xZi5MDPHI6z5SJkT8zD0ye73jPEjtsuNB8yw/edit?usp=sharing)
2. [Status of logic implementation in google sheets](https://docs.google.com/spreadsheets/d/1IMpNUJXqhcF_yXLiDHI4kB_OUodeH3qB-Y32fITV0s0/edit?usp=sharing)

### Priorities
1. [Priority for releasing](https://docs.google.com/spreadsheets/d/1PqqdhOZgQ4Nj9antMjUH505lcbAbho-EaRSMdcUEJis/edit?usp=sharing)

# App specific topics

### Main apps
[Fiori Tracker Core](/dev/ft-core.md) 

### Optional relations for Fiori Tracker
*System values relations*<br>
[FT Catalogs Relation: Apps As-is](/dev/ft-cats-rel-apps-asis.md) <br>
[FT Apps Relation: Catalogs, As-is](/dev/ft-apps-rel-catalogs-asis.md)

*Application usage relation*<br>
[FT Apps Relation: Apps' Usage](/dev/ft-apps-rel-appsusage.md) 

### Plugin for as-is information
[AsIs](/dev/asis.md) 

### Reports
1. [Catalog Apps Report](/dev/ca.md) - List of SAP Fiori apps assigned to a catalog in the chosen system
2. [App Catalogs Report](dev/ac.md) - List of SAP Fiori catalogs assigned to an app in the chosen system
3. [Fiori Apps' Usage Report](dev/fa.md) - List of top most used applications identified by semantic object and action


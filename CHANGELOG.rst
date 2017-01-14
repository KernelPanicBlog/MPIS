==========
Change Log
==========
All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.

[2.0-alpha] - 2017-1-13
===========
added:
______
* modulo Colorize (color para la consola)
* modulo Traslate (soporte para multi-idiomas)
* modulo para el manejo de la base de datos (Sqlite3)
* nueva forma para el manejo de los menus.
* se agrego la opcion dinamica tareas a la barra de opciones
* se extendio la funcionalidad de multi-install
ahora permite instalar, desinstalar y agregar comandos para ser ejecutados en lotes)
* and ... more

Changed:
______
* Se elimino el archivo de configuracion (.conf) las configuraciones estan ahora
en la base de datos
* los paquetes a instalar estan en una base de datos ahora.

Fixed:
______
*


[1.1.1] - 2016-10-13
===========
Changed:
______
* Fixing some sintactic words
* Fixing Telegram installation commands

Fixed:
______


[1.1] - 2016-10-13
===========
Changed:
______
* Fixing some sintactic words
* Fixing Telegram installation commands

Fixed:
______
* Issue #40

[1.0] - 2016-09-20
===========
added:
______
* Option "about" in the main menu
* Options bar
* parameter "--noconfirm" Default active
* option to configure the appearance
* Settings menu
* language Español (es)

Changed:
________
* Delete xml file --> now the menus are in a dictionary in the resource file.
* Restructuring and optimization of code

Fixed:
______
* issue #38

[0.3.0-alpha2] - 2016-08-29
===========
added:
______
* new funtions in API
* new funtions in Core
* suport for GUI QT

Changed:
________
* Delete option -> (update script).

[0.3.0-alpha1] - 2016-08-22
===========================
added:
______
* instructions to install and uninstall the beta and alpha version (in README file)
* Option to see the CHANGELOG file
* Support to  cancel commands that require root permissions [issue #27].
* added CHANGELOG file

Changed:
________
* the setup.py now installs the CHANGELOG file
* exception handling: IndexError
* pacman -Qe |less to pacman -Qe in xml file [issue #30]
* pacman-keys command to pacman-key in xml file [issue #28]

Fixed:
______
* issue #30 (pacman -Qe |less)
* issue #28 (pacman-keys command error)
* PKGBUILD AUR (MD5 and tag)
* issue #27 (uninformed use of root privileges).

[0.2.1] - 2016-08-21
====================
Added:
______
* MPIS logo.
* badges in README file.

Changed:
________
* reStructuredText adoption of the format for the readme file

Fixed:
______
* errors in the XML file

[0.2a] - 2016-08-17
===================
added:
______
* XML file for the menu options
* PKGBUILD
* Installation from the setup.py file
* Support for python 2.7 y python 3.x

Changed:
________
* Automation menus though a xml file
* Restructuring and optimization of code
* Name of project to MPIS

Security:
_________
* Implementation of the subprocess library

Fixed:
______
* issue #25 (xml file error)
* issue #23 (nemu back)
* issue #22 (setup file)
* issue #18 (use of branches)
* issue #15 (python 3)
* issue #14 (validate each command)
* issue #13 (show help each menu)
* issue #11 (option menu back work in all menus)
* issue #8 (the mirrorlist file contents will not be displayed)
* issue #6 (change the lenguage to english)
* issue #5 (install telegram fram the official website)
* issue #4 (clean the screen to make action)
* issue #3 (WPS not installed)

[0.1] - 2016-05-18
==================

Added:
______
* project start

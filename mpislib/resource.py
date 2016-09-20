#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of MPIS (https://github.com/KernelPanicBlog/MPIS).
#
# MPIS(Manjaro Post Installation Script) is free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License,
# or any later version.
#
# MPIS (Manjaro Post Installation Script):
# It allows  users to choose different options such as
# install an application or CONFIG some tools and environments.
#
# MPIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS; If not, see <http://www.gnu.org/licenses/>.
import os
###############################################################################
# MESSAGES
###############################################################################
MESSAGES_EN = {
    "msgLID": "Español (es)\nEnglish (en)",
    "msgIA": "{0}Restart to apply changes{1}",
    "msgID": "Languages available",
    "msgCN": "Select a color notifications",
    "msgCS": "Select a secondary color",
    "msgSCMO": "Select a color for the menus options",
    "msgbase": "Press any key to continue...",
    "msgSW": "Setup Wizard appearance..\n",
    "msgSCTM": "Select a color for the title menus",
    "msgAC": "\t Available colours:",
    "set-noconfirm": "\n The parameter setting is changed correctly",
    "Option-Bar": "\n{0}back (b), exit (e), help (h){1}",
    "msgMpis": "\n{0}Option > {1}",
    "msgTFWE": "Task finished with errors.",
    "msgTF": "Task finished.",
    "msgAur": "This application will be installed from the AUR "
              "repository (community).\nIt will be installed at "
              "your own risk.\n",
    "msgAurC": "You want to continue the Installation from yaourt? \n"
               "yes or not.",
    "msgSudo": "It is asked superuser permission to perform this action",
    "msgSudoC": "You want to continue? \nyes or not",
    "msgNf": "(not functional, yet)",
    "msgCtrl+C": "\nYou had press the Ctrl+C keys combination. Accepted exit "
                 "request. Bye!",
    "msgNOp": "Sorry not valid option.",
    "msgUserCancel": "The command was canceled by the user",
    "msgNoConfirm": "the '--noconfirm' parameter is enabled by default,"
                    "you can change this option in the Settings menu",
    "msgInvalidCmd": "\n{0}Invalid option canceling the command{1}",
    "msgEnd": """
            {0}Thanks for choosing us, we hope this script helped you.
            \t- The KernelPanicBlog Team.
            Our web: https://kernelpanicblog.wordpress.com{1}""",
    "msgHelp": """
{0}Help:{1}
\n{2}You can select an option with the given
number or write 3 shortcuts:
- back or b -> return to the previous option
- help or h -> show help
- exit or e or Ctrl+C -> finish the script execution{3}""",
    "banner": """
            {0} __  __ _____ _____  _____
            |  \/  |  __ \_   _|/ ____|
            | \  / | |__) || | | (___
            | |\/| |  ___/ | |  \___ \\
            | |  | | |    _| |_ ____) |
            |_|  |_|_|   |_____|_____/{1}""",
    "MPIS": "{0}\nManjaro Post Installation Script version 1.0.0-dev{1}",
    "Authors": """
{0}Authors:
SniferL4bs  | https://www.sniferl4bs.com
NeoRanger   | https://www.neositelinux.com.ar
Harrinsoft  | harrinsoft@gmail.com
Collaborative Blog: | https://kernelpanicblog.wordpress.com{1}""",
    "Report Bugs!": "\nPlease report bugs :) \t"
                    "https://github.com/KernelPanicBlog/MPIS/issues",
}

MESSAGES_ES = {
    "msgIA": "{0}Es necesario reiniciar para aplicar los cambios{1}",
    "msgLID": "Español (es)\nEnglish (en)",
    "msgID": "Idiomas Disponibles:",
    "msgCN": "Seleccione el color de las notificaciones",
    "msgCS": "Seleccione un color segundario",
    "msgSCMO": "Seleccione un color para las opciones del menu",
    "msgbase": "Pulse cualquier tecla para continuar ...",
    "msgSW": "Ayudante para la configuracion de la apariencia..\n",
    "msgSCTM": "Seleccione un color para los titulos de los menus",
    "msgAC": "\t Colores Disponibles:",
    "set-noconfirm": "\n El ajuste del parametro se cambio correctamente",
    "Option-Bar": "\n{0}back (b), exit (e), help (h){1}",
    "msgMpis": "\n{0}Opcion > {1}",
    "msgTFWE": "Tarea terminada con errores.",
    "msgTF": "Tarea terminada.",
    "msgAur": "Esta aplicacion sera instalada desde los repositorios"
              "(comunitarios) de AUR.\n Instalela bajo sus propio riesgo \n",
    "msgAurC": "Usted desea continuar con la instalacion desde yaourt? \n"
               "Si o no.",
    "msgSudo": "Se le pedira permisos de superusuario para realizar esta accion",
    "msgSudoC": "Usted desea continuar? \nSi ó no",
    "msgNf": "(No funcional, todavia)",
    "msgCtrl+C": "\nUsted ha presionado la combinacion de teclas Ctrl+C.\n"
                 "La solicitud de salida se ha aceptado. Adios!",
    "msgNOp": "Lo sentimos esta opcion no es valida",
    "msgUserCancel": "El Comando ha sido cancelado por el Usuario",
    "msgNoConfirm": "El parametro '--noconfirm' esta activo por defecto,"
                    "Usted puede cambiar esta opcion en el menu de "
                    "configuracion",
    "msgInvalidCmd": "\n{0}Opcion invalida, cancelando el comando{1}",
    "msgEnd": """
            {0}Gracias por elegirnos, Esperamos haber sido de ayuda.
            \t- El equipo KernelPanicBlog.
            Nuestra web: https://kernelpanicblog.wordpress.com{1}""",
    "msgHelp": """
{0}Help:{1}
\n{2}Usted puede selecionar una opcion con
los numeros dados ó escribir 3 atajos:
- back or b -> Regresa a la opcion anterior
- help or h -> Muestra la ayuda
- exit or e or Ctrl+C -> Termina la ejecucion del script{3}""",
    "banner": """
            {0} __  __ _____ _____  _____
            |  \/  |  __ \_   _|/ ____|
            | \  / | |__) || | | (___
            | |\/| |  ___/ | |  \___ \\
            | |  | | |    _| |_ ____) |
            |_|  |_|_|   |_____|_____/{1}""",
    "MPIS": "{0}\nManjaro Post Installation Script version 1.0.0-dev{1}",
    "Authors": """
{0}Autores:
SniferL4bs  | https://www.sniferl4bs.com
NeoRanger   | https://www.neositelinux.com.ar
Harrinsoft  | harrinsoft@gmail.com
Blog Colaborativo: | https://kernelpanicblog.wordpress.com{1}""",
    "Report Bugs!": "\nPor Favor reporte los fallos! :) \t"
                    "https://github.com/KernelPanicBlog/MPIS/issues",
}

ERRORS_EN = {
    "0x001": "{0}Command not found{1}",
    "0x002": "{0}Command exited with errors{1}",
    "0x003": "{0}Error in option, this value is outside the range of the list{1}"
    }
ERRORS_ES = {
    "0x001": "{0}No se encontro el comando{1}",
    "0x002": "{0}Error al ejecutar el comando{1}",
    "0x003": "{0}Error en opcion, este valor esta fuera del rango de la lista{1}"
    }
###############################################################################
# COLORS
###############################################################################
COLORS = {
    "White": ("\033[1;30m", "\033[1;m"),
    "Red": ("\033[1;31m", "\033[1;m"),
    "Yellow": ("\033[1;33m", "\033[1;m"),
    "Green": ("\033[1;36m", "\033[1;m"),
    "Blue": ("\033[1;34m", "\033[1;m"),
    "Purple": ("\033[1;35m", "\033[1;m"),
    "Gray": ("\033[1;37m", "\033[1;m"),
    "Green-2": ("\033[1;32m", "\033[1;m"),
    "Highlighted": ("\033[1;46m\033[1;30m", "\033[1;m\033[1;m")
}
###############################################################################
# PATH
###############################################################################
HOME_PATH = os.getenv("HOME")
PATH_FILE = "/usr/share/mpis"
###############################################################################
# Funciones
###############################################################################


def get_path_config():
    global HOME_PATH

    return HOME_PATH + "/.mpisconfig"


def get_path_file(_name):
    global PATH_FILE

    return os.path.join(PATH_FILE, _name)


def get_all_colors():
    global COLORS

    return COLORS


def get_color(name_color):

    global COLORS

    return COLORS.get(name_color)


def get_error(name_error, lan):
    global ERRORS_ES
    global ERRORS_EN

    return ERRORS_EN.get(name_error) if lan == "en" else ERRORS_ES.get(name_error)


def get_message(name_msg, lan):
    global MESSAGES_EN
    global MESSAGES_ES

    return MESSAGES_EN.get(name_msg) if lan == "en" else MESSAGES_ES.get(name_msg)


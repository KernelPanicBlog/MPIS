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
MESSAGES = {
    "set-noconfirm": "\n the parameter setting is changed correctly",
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
\nYou can select an option with the given
number or write 3 shortcuts:
- back or b -> return to the previous option
- help or h -> show help
- exit or e or Ctrl+C -> finish the script execution""",
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

ERRORS = {
    "0x001": "{0}command not found{1}",
    "0x002": "{0}command exited with errors{1}",
    "0x003": "{0}Error in option, this value is outside the range of the list{1}"
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

###############################################################################
# Funciones
###############################################################################


def get_path_config():
    global HOME_PATH

    return HOME_PATH + "/.mpisconfig"


def get_all_colors():
    global COLORS

    return COLORS


def get_color(name_color):

    global COLORS

    return COLORS.get(name_color)


def get_error(name_error):
    global ERRORS

    return ERRORS.get(name_error)


def get_message(name_msg):
    global MESSAGES

    return MESSAGES.get(name_msg)


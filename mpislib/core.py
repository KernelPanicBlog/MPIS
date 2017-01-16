#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
# This file is part of MPIS (https://github.com/KernelPanicBlog/MPIS).
#
# MPIS(Manjaro Post Installation Script) is free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License,or
# any later version.
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
# ______________________________________________________________________________
import subprocess
import mpislib
from mpislib.colorize import colorize
from mpislib.colorize import (Estilo, Texto, Fondo)
from mpislib.traslate import tr
from mpislib.db import Database
from mpislib.resource import Resource
# -----------------------------------------------------------------------------
# Variables Globales
# -----------------------------------------------------------------------------
resource = Resource()
db = Database(resource.path_db())
# -----------------------------------------------------------------------------
# Clases
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Funciones
# -----------------------------------------------------------------------------


def user_input():
    try:
        return input(colorize.aplicar(1, db.get_config("user_input"))
                     + tr("Option >") + colorize.reset())
    except ValueError:
        return 0


def pause(_msg=""):
    try:
        _base_msg = tr("Press any key to continue...")
        _colour = db.get_config("notifications_colour")
        return str(input(colorize.aplicar(1, _colour)
                         + _msg + "\n" + _base_msg))
    except SyntaxError:
        pass


def clear():
    subprocess.run(["clear"])


def sleep(_time):
    """hace una pausa la cantidad de segundos indicados por _time
    Args:
        _time (int): tiempo de la pausa en segundos
    """
    subprocess.run(["sleep", str(_time)+"s"])


def mkopts(_option):
    upper = _option.upper()
    lower = _option.lower()
    lfirst = _option[0].lower()
    ufirst = _option[0].upper()
    tfirst = _option.capitalize()
    return [upper, lower, lfirst, ufirst, tfirst]


def show_banner(do_clear=True):
    if do_clear: clear()
    banner = """
         __  __ _____ _____  _____
        |  \/  |  __ \_   _|/ ____|
        | \  / | |__) || | | (___
        | |\/| |  ___/ | |  \___ \\
        | |  | | |    _| |_ ____) |
        |_|  |_|_|   |_____|_____/"""
    MPIS = "\tManjaro Post Install Script V" + str(mpislib.__version__)
    autor = mpislib.__autores__
    print(colorize.aplicar(Estilo.negrita.value, Texto.cian.value) + banner)
    print(MPIS + "\n")
    print(autor + colorize.reset())


def execute_command(command, sequentially=True):
    error_flag = False
    cancel_by_user_flag = False
    memory_option = False
    for cmd in command:
        try:
            if cmd[0] in ["yaourt", "sudo"]:
                if not memory_option:
                    if cmd[0] == "yaourt":
                        print(tr("This application will be installed from the AUR repository (community)."))
                        print(tr("It will be installed at your own risk."))
                        print(tr("You want to continue the installation from AUR?."))
                        print(tr("yes or not."))
                    elif cmd[0] == "sudo":
                        print(tr("It is asked superuser permission to perform this action."))
                        print(tr("You want to continue?"))
                        print(tr("yes or not."))
                    option = user_input()
                    if option in mkopts(tr("yes")):
                        memory_option = True
                    elif option in mkopts(tr("not")):
                        cancel_by_user_flag = True
                        break
                    else:
                        colour = db.get_config("notifications_colour")
                        print(colorize.aplicar(Estilo.negrita, colour)
                              + tr("Invalid option, canceled command.")
                              + colorize.reset())
                        cancel_by_user_flag = True
                        sequentially = True
                        error_flag = True
            if not error_flag and sequentially:
                if subprocess.check_call(cmd.split()) == 0:
                    error_flag = False
                else:
                    error_flag = True
                    break
            elif not error_flag or not sequentially:
                if subprocess.check_call(cmd.split()) == 0:
                    error_flag = False
                else:
                    error_flag = True
        except subprocess.CalledProcessError:
            error_flag = True
            colour = db.get_config("notifications_colour")
            print(colorize.aplicar(Estilo.negrita.value, colour)
                  + tr("Command exited with errors.")
                  + colorize.reset())
    if not error_flag and not cancel_by_user_flag:
        pause(tr("Task finished."))
    elif cancel_by_user_flag:
        pause(tr("The command was canceled by the user."))
    else:
        pause(tr("Task finished with errors."))


def menu_config(_conf, _title, _text_option, fondo=False):
    title_text_colur = db.get_config("title_text_colour")
    title_back_colur = db.get_config("title_back_colour")
    title = colorize.aplicar(Estilo.negrita.value, title_text_colur,
                             title_back_colur)
    title += tr(_title) + colorize.reset()
    barra = "████████" if not fondo else "________"
    clear()
    ok = False
    while not ok:
        print("\t" + title)
        print(tr(_text_option))
        print(tr("Available colours:"))
        for color in (Texto if not fondo else Fondo):
            string = colorize.aplicar(Estilo.negrita.value,
                                      color.value if not fondo else Texto.reset.value,
                                      Fondo.reset.value if not fondo else color.value)
            string += "{0}) {1}".format(color.value, barra) + colorize.reset()
            print(string)
        _option = user_input()
        if int(_option) in [val.value for val in (Texto if not fondo else Fondo)]:
            db.update_config(_conf, _option)
            ok = True
            clear()
        else:
            ok = False
            clear()


def wizard_config():
    # color del texto de los titulos
    menu_config("title_text_colour",
                "Setup Wizard appearance.",
                "Select a colour for the title menu.")

    # color de fondo de los titulos
    menu_config("title_back_colour",
                "Setup Wizard appearance.",
                "Select a colour for the back title menu.",
                True)

    # color del texto de las opciones
    menu_config("option_menu_colour",
                "Setup Wizard appearance.",
                "Select a colour for the menus options.")

    # color del texto de las notificaciones
    menu_config("notifications_colour",
                "Setup Wizard appearance.",
                "Select a colour notifications.")

    # color del texto para los inputs
    menu_config("user_input",
                "Setup Wizard appearance.",
                "Select a secondary colour.")


def set_language():
    notifications_colour = db.get_config("notifications_colour")
    text_colour = db.get_config("option_menu_colour")
    ok = False
    while not ok:
        string = colorize.aplicar(Estilo.negrita.value, text_colour)
        string += tr("Languages available")
        print(string)
        print(tr("Spanish (es)."))
        print(tr("English (en)."))
        _option = user_input()
        if _option in ["es", "en", tr("Español"), tr("English")]:
            if _option in ["es", tr("Español")]:
                db.update_config("language", "\"ES_es\"")
                ok = True
            else:
                db.update_config("language", "\"EN_us\"")
                ok = True
    string = colorize.aplicar(Estilo.negrita.value, notifications_colour)
    string += tr("The parameter was changed correctly.")
    print(string)
    print("\n" + tr("Restart to apply changes.") + colorize.reset())
    sleep(1)


def toggle_config(_config):
    notifications_colour = db.get_config("notifications_colour")
    string = colorize.aplicar(Estilo.negrita.value, notifications_colour)
    string += tr("The parameter was changed correctly.")
    value = db.get_config(_config)
    db.update_config(_config, "\"False\"" if value == "True" else "\"True\"")
    print(string)
    sleep(1)

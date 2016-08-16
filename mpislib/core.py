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
# install an application or config some tools and environments.
#
# MPIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS; If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import subprocess
from xml.etree.ElementTree import *

messages = {
    "msgMpis": "\n\033[1;32mOption > \033[1;m",
    "msgTFWE": "Task finished with errors. Press Enter to continue...",
    "msgTF": "Task finished. Press Enter to continue...",
    "msgAur": "This application will be installed from the AUR "
              "repository (community). It will be installed at "
              "your own risk.",
    "msgNf": "(not functional, yet)",
    "msgCtrl+C": "\nYou had press the Ctrl+C keys combination. Accepted exit "
                 "request. Bye!",
    "msgNOp": "Sorry not valid option, Press any key to continue..."
    }

errors = {
    "0x001": "command not found",
    "0x002": "command exited with errors"
    }


def execute_command(command, option=False):
    error_flag = False
    for cmd in command:
        try:
            cmd = cmd.split()
            if cmd[0] in ["yaourt"]:
                print(messages["msgAur"])
            if not error_flag and option:
                if subprocess.check_call(cmd) == 0:
                    error_flag = False
                else:
                    error_flag = True
                    break
            elif not error_flag or not option:
                if subprocess.check_call(cmd) == 0:
                    error_flag = False
                else:
                    error_flag = True
        except subprocess.CalledProcessError:
            error_flag = True
            print(errors["0x002"])
    if not error_flag:
        pause(messages["msgTF"])
    else:
        pause(messages["msgTFWE"])


def user_input():
    try:
        return input(messages["msgMpis"])
    except ValueError:
        return 0


def pause(msg="Press any key to continue..."):
    try:
        a = str(input(msg))
    except SyntaxError:
        pass


def mkopts(option):
    upper = option.upper()
    lower = option.lower()
    lfirst = option[0].lower()
    ufirst = option[0].upper()
    tfirst = option.capitalize()
    return [upper, lower, lfirst, ufirst, tfirst]


def clear():
    subprocess.run(["clear"])


def sleep():
    subprocess.run(["sleep", "2s"])


def end_message(do_clear=True, shutdown=True, value=0):
    if do_clear: clear()
    print("""\033[1;36m
Thanks for choosing us, we hope this script helped you.
    - The KernelPanicBlog Team.
Our web: https://kernelpanicblog.wordpress.com
\033[1;m""")
    if shutdown: sys.exit(value)


def show_banner(do_clear=True):
    if do_clear: clear()
    print("""\033[1;36m
 __  __ _____ _____  _____
|  \/  |  __ \_   _|/ ____|
| \  / | |__) || | | (___
| |\/| |  ___/ | |  \___ \\
| |  | | |    _| |_ ____) |
|_|  |_|_|   |_____|_____/

Manjaro Post Installation Script version 0.2a
\033[1;m
\033[1;32m
Authors:
    SniferL4bs  | https://www.sniferl4bs.com
    NeoRanger   | https://www.neositelinux.com.ar
    Harrinsoft  | harrinsoft@gmail.com
Collaborative Blog: | https://kernelpanicblog.wordpress.com
\033[1;m
Script in testing phase, please report bugs :)
https://github.com/KernelPanicBlog/MPIS/issues
""")
    pause()
    clear()


def show_help(do_clear=True):
    if do_clear: clear()
    print("""\033[1;36m
Help:
\033[1;m
You can select an option with the given
number or write 3 shortcuts:
- back or b -> return to the previous option
- help or h -> show help
- exit or e or Ctrl+C -> finish the script execution
""")
    pause()
    clear()


def search_commands(name_app, l_apps):
    for c in range(len(l_apps)):
        if l_apps[c].name == name_app:
            return l_apps[c]
            break
    return None


def search_menu(name_menu, l_menus):
    for c in range(len(l_menus)):
        if l_menus[c].name == name_menu:
            return c
            break
    return 0


def not_repeated(name_cmd, l_apps):
    for c in range(len(l_apps)):
        if l_apps[c].name == name_cmd:
            return True
            break
    return False


class Item:
    def __init__(self):
        self.name = ""
        self.title = ""
        self.option = 0
        self.ismenu = "False"


class Menu:
    def __init__(self):
        self.name = ""
        self.title = ""
        self.items = []


class App:
    def __init__(self):
        self.name = ""
        self.sequentially = False
        self.commands = []
        self.messages = []


class Mpis:
    def __init__(self):
        self.menus = []
        self.apps = []
        self.__load_config()

    def __load_config(self):
        root_dir = "/usr/lib/mpis/"
        file_name = "menu.xml"
        root_file = root_dir + file_name
        menu_config = file_name if not os.path.exists(root_file) else root_file
        with open(menu_config) as f:
            uncode = f.read()
            data = fromstring(uncode)
            lst_menus = data.findall("menu")
        for n_menu in lst_menus:
            new_menu = Menu()
            new_menu.name = n_menu.find("name").text
            new_menu.title = n_menu.find("title").text
            lst_items = []
            items = n_menu.findall("items/item")
            for item in items:
                new_item = Item()
                new_item.title = item.find("title").text
                new_item.name = item.find("name").text
                new_item.option = item.find("option").text
                new_item.ismenu = item.get("ismenu")
                commands = item.findall("commands")
                if len(commands) != 0:
                    if not not_repeated(item.find("name").text, self.apps):
                        new_app = App()
                        new_app.name = item.find("name").text
                        print(commands[0].get("sequentially"))
                        if commands[0].get("sequentially") == "True":
                            new_app.sequentially = True
                        else:
                            new_app.sequentially = False
                        lst_cmd = []
                        for cmd in commands:
                            all_cmd = cmd.findall("cmd")
                            for c in all_cmd:
                                lst_cmd.append(c.text)
                        new_app.commands = lst_cmd
                        self.apps.append(new_app)
                lst_items.append(new_item)
            new_menu.items = lst_items
            self.menus.append(new_menu)

    def reload(self):
        self.__load_config()

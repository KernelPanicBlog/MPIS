#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from xml.etree.ElementTree import *

messages = {
    'msgMpis': "\t\033[1;32mOption > \033[1;m",
    'msgTFWE': "Task finished with errors. Press Enter to continue...",
    'msgTF': "Task finished. Press Enter to continue...",
    'msgAur': "This application will be installed from the AUR "
              "repository (community). It will be installed at "
              "your own risk.",
    'msgNf': "(not functional, yet)",
    'msgCtrl+C': "\nYou had press the Ctrl+C keys combination. Accepted exit "
                 "request. Bye!",
    'msgNOp': "Sorry not valid option, Press any key to continue..."
    }

errors = {
    '0x001': 'command not found'
    }


def execute_command(command, option="False"):
    flat = True
    for cmd in command:
        if cmd.startswith("yaourt"):
            print(messages['msgAur'])
        if flat and option == "True":
            if os.system(cmd) == 0:
                flat = True
            else:
                flat = False
                break
        elif flat or option != "True":
            if os.system(cmd) == 0:
                flat = True
            else:
                flat = False
    if flat:
        pause(messages['msgTF'])
    else:
        pause(messages['msgTFWE'])


def user_input():
        try:
            return input(messages['msgMpis'])
        except ValueError:
            return 0


def pause(msg="Press any key to continue..."):
    try:
        a = str(input(msg))
    except SyntaxError:
        pass


def clear():
    os.system("clear")


def end_message():
    print("""\033[1;36m
\tThanks for choosing us, we hope this script helped you.
\t\t- The KernelPanicBlog Team.
\tOur web: https://kernelpanicblog.wordpress.com\033[1;m
""")


def banner():

    print("""\033[1;36m
  __  __ _____ _____  _____ 
 |  \/  |  __ \_   _|/ ____|
 | \  / | |__) || | | (___  
 | |\/| |  ___/ | |  \___ \ 
 | |  | | |    _| |_ ____) |
 |_|  |_|_|   |_____|_____/ \033[1;m
\t\033[1;36mManjaro Post Installation Script version 0.2a\033[1;m
\t\033[1;32mAuthors:\033[1;m
\t\t\033[1;32mSniferL4bs  | https://www.sniferl4bs.com\033[1;m
\t\t\033[1;32mNeoRanger   | https://www.neositelinux.com.ar\033[1;m
\t\t\033[1;32mHarrinsoft  | harrinsoft@gmail.com                 \033[1;m
\t\033[1;32mCollaborative Blog: | https://kernelpanicblog.wordpress.com\033[1;m

\tScript in testing phase, please report bugs :)
""")


def help():
    print("""\n\033[1;36mHelp:\033[1;m\n
\tYou can select an option with the given
\tnumber or write 3 shortcuts:
\t- back or b-> return to the previous option
\t- help or h->
\t- exit or Ctrl+C or x-> finish the script execution
""")


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
        self.ismenu = 'False'


class Menu:
    def __init__(self):
        self.name = ""
        self.title = ""
        self.items = []


class App:
    def __init__(self):
        self.name = ""
        self.sequentially = "False"
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
            lst_menus = data.findall('menu')
        for n_menu in lst_menus:
            new_menu = Menu()
            new_menu.name = n_menu.find('name').text
            new_menu.title = n_menu.find('title').text
            lst_items = []
            items = n_menu.findall('items/item')
            for item in items:
                new_item = Item()
                new_item.title = item.find('title').text
                new_item.name = item.find('name').text
                new_item.option = item.find('option').text
                new_item.ismenu = item.get('ismenu')
                commands = item.findall('commands')
                if len(commands) != 0:
                    if not not_repeated(item.find('name').text, self.apps):
                        new_app = App()
                        new_app.name = item.find('name').text
                        new_app.sequentially = item.get('sequentially')
                        lst_cmd = []
                        for cmd in commands:
                            all_cmd = cmd.findall('cmd')
                            for c in all_cmd:
                                lst_cmd.append(c.text)
                        new_app.commands = lst_cmd
                        self.apps.append(new_app)
                lst_items.append(new_item)
            new_menu.items = lst_items
            self.menus.append(new_menu)

    def reload(self):
        self.__load_config()

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
###############################################################################
import sys
import platform
import subprocess
from configparser import ConfigParser
from mpislib.menus import find_menu
from mpislib.packages import get_action
from mpislib.packages import get_packages
from mpislib.packages import get_alias
from mpislib.packages import get_category
from mpislib.resource import get_message
from mpislib.resource import get_color
from mpislib.resource import get_error
from mpislib.resource import get_path_config
from mpislib.resource import get_all_colors

###############################################################################
# GLOBAL CONF
###############################################################################
CONFIG = ConfigParser()

###############################################################################
# Clases
###############################################################################


class Node:
    def __init__(self, _name, _parent=None):
        self.__name = _name
        self.__parent = _parent
        self.__childern = []

    @property
    def parent(self):
        return self.__parent

    @property
    def childern(self):
        return self.__childern

    @property
    def name(self):
        return self.__name

    def add_childern(self, child):
        if isinstance(child, str):
            self.__childern.append(Node(child, self.name))
        elif isinstance(child, Node):
            self.__childern.append(child)

    def __getitem__(self, _item):
        return self.__childern[_item]

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return '{}'.format(self.name)

###############################################################################
# Funciones
###############################################################################


def read_config():
    global CONFIG
    if not CONFIG.read(get_path_config()):
        set_default_config()


def set_default_config():
    global CONFIG

    CONFIG['General'] = {
        'noconfirm': "True",
        'language': "en"
        }
    CONFIG['Appearance'] = {
        'menu-title': "Highlighted",
        'option-menu': "Green",
        'user-input': "Green-2",
        'notifications': "Red"
        }
    with open(get_path_config(), "w") as config_file:
        CONFIG.write(config_file)


def save_config():
    global CONFIG

    with open(get_path_config(), "w") as config_file:
        CONFIG.write(config_file)


def get_language():
    global CONFIG

    return CONFIG['General'].get('language')


def toggle_noconfirm():
    global CONFIG

    _noconfirm = CONFIG['General'].getboolean('noconfirm')
    CONFIG['General']['noconfirm'] = "False" if _noconfirm else "True"
    pause(get_message("set-noconfirm"))
    save_config()


def set_language():
    global CONFIG
    language = CONFIG['General'].get('language')
    appearance = CONFIG['Appearance']
    ok = False
    while not ok:
        print(get_message("msgID", language))
        print(get_message("msgLID", language))
        _option = user_input()
        if _option in ["es", "en", "Español", "English"]:
            if _option in ["es", "Español"]:
                CONFIG['General']['language'] = "es"
                ok = True
            else:
                CONFIG['General']['language'] = "en"
                ok = True
    save_config()
    prefix_color, suffix_color = get_color(appearance.get('notifications'))
    pause(get_message("msgIA", language).format(prefix_color, suffix_color))


def wizard_config():
    global CONFIG
    language = CONFIG['General'].get('language')
    pause(get_message("msgSW", language))
    clear()
    ok = False
    while not ok:
        print(get_message("msgSCTM", language))
        print(get_message("msgAC", language))
        for color in get_all_colors().keys():
            prefix_color, suffix_color = get_color(color)
            print('\t{0}{2}{1}'.format(prefix_color, suffix_color, color))
        _option = user_input()
        if _option.capitalize() in get_all_colors().keys():
            CONFIG['Appearance']['menu-title'] = _option.capitalize()
            ok = True
            clear()
        else:
            ok = False
            clear()
    ok = False
    while not ok:
        print(get_message("msgSCMO", language))
        print(get_message("msgAC", language))
        for color in get_all_colors().keys():
            prefix_color, suffix_color = get_color(color)
            print('\t{0}{2}{1}'.format(prefix_color, suffix_color, color))
        _option = user_input()
        if _option.capitalize() in get_all_colors().keys():
            CONFIG['Appearance']['option-Menu'] = _option.capitalize()
            ok = True
            clear()
        else:
            ok = False
            clear()
    ok = False
    while not ok:
        print(get_message("msgCS", language))
        print(get_message("msgAC", language))
        for color in get_all_colors().keys():
            prefix_color, suffix_color = get_color(color)
            print('\t{0}{2}{1}'.format(prefix_color, suffix_color,
                                       color))
        _option = user_input()
        if _option.capitalize() in get_all_colors().keys():
            CONFIG['Appearance']['user-input'] = _option.capitalize()
            ok = True
            clear()
        else:
            ok = False
            clear()
    ok = False
    while not ok:
        print(get_message("msgCN", language))
        print(get_message("msgAC", language))
        for color in get_all_colors().keys():
            prefix_color, suffix_color = get_color(color)
            print('\t{0}{2}{1}'.format(prefix_color, suffix_color,
                                       color))
        _option = user_input()

        if _option.capitalize() in get_all_colors().keys():
            CONFIG['Appearance']['notifications'] = _option.capitalize()
            ok = True
            clear()
        else:
            ok = False
            clear()

    save_config()


def execute_command(command, sequentially=True):
    global CONFIG
    appearance = CONFIG['Appearance']
    language = CONFIG['General'].get('language')
    error_flag = False
    cancel_by_user_flag = False
    memory_option = False
    for cmd in command:
        try:
            if cmd[0] in ["yaourt", "sudo"]:
                if not memory_option:
                    if cmd[0] == "yaourt":
                        print(get_message("msgAur", language))
                        print(get_message("msgAurC", language))
                    elif cmd[0] == "sudo":
                        print(get_message("msgSudo", language))
                        print(get_message("msgSudoC", language))
                    option = user_input()
                    if option in mkopts("yes"):
                        memory_option = True
                    elif option in mkopts("not"):
                        cancel_by_user_flag = True
                        break
                    else:
                        prefix_color, suffix_color = get_color(
                            appearance.get('notifications')
                        )
                        print(get_message("msgInvalidCmd", language).format(
                            prefix_color,
                            suffix_color)
                        )
                        cancel_by_user_flag = True
                        sequentially = True
                        error_flag = True
            if not error_flag and sequentially:
                if subprocess.check_call(cmd) == 0:
                    error_flag = False
                else:
                    error_flag = True
                    break
            elif not error_flag or not sequentially:
                if subprocess.check_call(cmd) == 0:
                    error_flag = False
                else:
                    error_flag = True
        except subprocess.CalledProcessError:
            error_flag = True
            show_error("0x002")
    if not error_flag and not cancel_by_user_flag:
        pause(get_message("msgTF", language))
    elif cancel_by_user_flag:
        pause(get_message("msgUserCancel", language))
    else:
        pause(get_message("msgTFWE", language))


def end_message(do_clear=True, shutdown=True, value=0):
    global CONFIG
    appearance = CONFIG['Appearance']
    language = CONFIG['General'].get('language')
    if do_clear:
        clear()
    prefix_color, suffix_color = get_color(appearance.get('option-menu'))
    print(get_message("msgEnd", language).format(prefix_color, suffix_color))
    if shutdown:
        sys.exit(value)


def show_banner(do_clear=True):
    language = CONFIG['General'].get('language')
    if do_clear:
        clear()
    prefix_color, suffix_color = get_color("Green")
    print(get_message("banner", language).format(prefix_color, suffix_color))
    prefix_color, suffix_color = get_color("Green")
    print(get_message("MPIS", language).format(prefix_color, suffix_color))
    prefix_color, suffix_color = get_color("Green-2")
    pause(get_message("Authors", language).format(prefix_color, suffix_color))
    clear()


def pause(msg):
    language = CONFIG['General'].get('language')
    try:
        _base_msg = get_message("msgbase", language)
        a = str(input(msg + '\n' + _base_msg))
    except SyntaxError:
        pass


def clear():
    subprocess.run(["clear"])


def sleep():
    subprocess.run(["sleep", "2s"])


def show_error(error_name):
    global CONFIG
    language = CONFIG['General'].get('language')
    appearance = CONFIG['Appearance']
    prefix_color, suffix_color = get_color(appearance.get('notifications'))
    print(get_error(error_name, language).format(prefix_color, suffix_color))


def show_help(do_clear=True):
    global CONFIG
    appearance = CONFIG['Appearance']
    language = CONFIG['General'].get('language')
    if do_clear:
        clear()
    prefix_color, suffix_color = get_color(appearance.get('menu-title'))
    prefix_color2, suffix_color2 = get_color(appearance.get('option-menu'))
    pause(get_message("msgHelp", language).format(prefix_color,
                                                  suffix_color,
                                                  prefix_color2,
                                                  suffix_color2)
          )
    clear()


def mkopts(_option):
    upper = _option.upper()
    lower = _option.lower()
    lfirst = _option[0].lower()
    ufirst = _option[0].upper()
    tfirst = _option.capitalize()
    return [upper, lower, lfirst, ufirst, tfirst]


def user_input():
    global CONFIG
    appearance = CONFIG['Appearance']
    language = CONFIG['General'].get('language')
    try:
        prefix, suffix = get_color(appearance.get('user-input'))
        return input(get_message("msgMpis", language).format(prefix, suffix))
    except ValueError:
        return 0


def add_childern(_node):
    global CONFIG
    language = CONFIG['General'].get('language')
    childern = find_menu(_node.name, language)
    if childern is not None:
        for child in childern:
            if child[1]:
                new_node = Node(child[0], _node.name)
                _node.add_childern(new_node)
                add_childern(new_node)
            elif child[0] == "incategory":
                childern_to_add = get_category(_node.name,
                                               _node.parent,
                                               language)
                for h in childern_to_add:
                    _node.add_childern(h[0])
            else:
                _node.add_childern(child[0])


def make_menus():
    """ Crea el arlbol de los menus """
    global CONFIG
    language = CONFIG['General'].get('language')
    menumake = Node("root")

    menumake.add_childern(
        Node("Main Menu" if language == "en" else "Menu principal",
             menumake.name)
    )
    # menumake.add_childern(
    #   Node("Main Menu",
    #      menumake.name) if language == "en" else Node("Menu principal",
    #                                                   menumake.name))

    add_childern(menumake.childern[0])

    return menumake


def get_arch():
    """Devuelve int(32) si el sistema es 32-bits o int(64) si es 64-bits"""

    arch, _ = platform.architecture()

    return int(arch[:2])


def get_noconfirm():
    global CONFIG

    return CONFIG['General'].getboolean('noconfirm')


def get_command(_menu, _option, _format="str"):
    """
    """
    global CONFIG
    general = CONFIG['General']
    suffix = "" if general.get('noconfirm') != "on" else " --noconfirm"
    commands = []
    name_app = _menu.childern[_option].name
    list_name = name_app.split()
    action = list_name[0]
    if action in ["Install", "Uninstall", "Instalar", "Desinstalar"]:
        if action == "Install":
            name_app = "{}" + name_app[len("Install"):]
        elif action == "Instalar":
            name_app = "{}" + name_app[len("Instalar"):]
        elif action == "Uninstall":
            name_app = "{}" + name_app[len("Uninstall"):]
        elif action == "Desinstalar":
            name_app = "{}" + name_app[len("Desinstalar"):]
        _app = get_packages(name_app)
        prefix = ""
        if _app[0] == "pacman":
            prefix = "sudo"
            suffix = ""
        elif _app[0] == "web":
            for pack in _app[2]:
                cmd = pack.format(get_arch())
                commands.append(cmd.split() if _format == "list" else cmd)
            return commands
        for pack in _app[2]:
            cmd = prefix + " " + _app[0] + " " + get_action(action) \
                  + " " + pack + suffix
            commands.append(cmd.split() if _format == "list" else cmd)
    else:
        _app = get_alias(name_app)
        for pack in _app:
            commands.append(pack.split() if _format == "list" else pack)
    return commands


def show_menu(_menu):
    global CONFIG
    appearance = CONFIG['Appearance']
    language = CONFIG['General'].get('language')
    under_line = "----"
    # Menu Title highlighted
    prefix_color, suffix_color = get_color(appearance.get('menu-title'))
    print("{0}# {1} #{2}".format(prefix_color,
                                 _menu.name,
                                 suffix_color)
          )
    prefix_color, suffix_color = get_color(appearance.get('option-menu'))
    print("{0}{1}{2}".format(prefix_color,
                             under_line + len(_menu.name) * "-",
                             suffix_color))
    # Options Menu
    for item, index in zip(_menu.childern,
                           range(len(_menu.childern))):
        print("{0}{1}) {2}{3}".format(prefix_color,
                                      index,
                                      item,
                                      suffix_color)
              )
    # Option Bar highlighted
    prefix_color, suffix_color = get_color(appearance.get('menu-title'))
    print(get_message("Option-Bar", language).format(prefix_color,
                                                     suffix_color)
          )


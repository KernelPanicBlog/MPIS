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

from mpislib.menus import find_menu
from mpislib.packages import get_action
from mpislib.packages import get_packages
from mpislib.packages import get_alias
from mpislib.packages import get_category
from mpislib.resource import get_message
from mpislib.resource import get_color
from mpislib.resource import get_error
from mpislib.resource import get_all_colors
from mpislib.config import get_config
from mpislib.config import get_section
from mpislib.config import update_config


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


def toggle_noconfirm():
    language = get_config('General', 'language')
    _noconfirm = bool(get_config('General', 'noconfirm'))
    update_config('General', 'noconfirm', "False" if _noconfirm else "True")
    pause(get_message("set-noconfirm", language))


def set_language():
    language = get_config('General', 'language')
    appearance = get_section('Appearance')
    ok = False
    while not ok:
        print(get_message("msgID", language))
        print(get_message("msgLID", language))
        _option = user_input()
        if _option in ["es", "en", "Español", "English"]:
            if _option in ["es", "Español"]:
                update_config('General', 'language', "es")
                ok = True
            else:
                update_config('General', 'language', "en")
                ok = True
    prefix_color, suffix_color = get_color(appearance.get('notifications'))
    pause(get_message("msgIA", language).format(prefix_color, suffix_color))


def wizard_config():
    language = get_config('General', 'language')
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
            update_config('Appearance', 'menu-title', _option.capitalize())
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
            update_config('Appearance', 'option-Menu', _option.capitalize())
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
            update_config('Appearance', 'user-input', _option.capitalize())
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
            update_config('Appearance', 'notifications', _option.capitalize())
            ok = True
            clear()
        else:
            ok = False
            clear()


def execute_command(command, sequentially=True):
    appearance = get_section('Appearance')
    language = get_config('General', 'language')
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
                    if option in mkopts("yes" if language == "en" else "si"):
                        memory_option = True
                    elif option in mkopts("not" if language == "en" else "no"):
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
    appearance = get_section('Appearance')
    language = get_config('General', 'language')
    if do_clear:
        clear()
    prefix_color, suffix_color = get_color(appearance.get('option-menu'))
    print(get_message("msgEnd", language).format(prefix_color, suffix_color))
    if shutdown:
        sys.exit(value)


def show_banner(do_clear=True):
    language = get_config('General', 'language')
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
    language = get_config('General', 'language')
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
    language = get_config('General', 'language')
    appearance = get_section('Appearance')
    prefix_color, suffix_color = get_color(appearance.get('notifications'))
    print(get_error(error_name, language).format(prefix_color, suffix_color))


def show_help(do_clear=True):
    appearance = get_section('Appearance')
    language = get_config('General', 'language')
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
    appearance = get_section('Appearance')
    language = get_config('General', 'language')
    try:
        prefix, suffix = get_color(appearance.get('user-input'))
        return input(get_message("msgMpis", language).format(prefix, suffix))
    except ValueError:
        return 0


def add_childern(_node):
    language = get_config('General', 'language')
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
    language = get_config('General', 'language')
    menumake = Node("root")

    menumake.add_childern(
        Node("Main Menu" if language == "en" else "Menu principal",
             menumake.name)
    )

    add_childern(menumake.childern[0])

    return menumake


def get_arch():
    """Devuelve int(32) si el sistema es 32-bits o int(64) si es 64-bits"""

    arch, _ = platform.architecture()

    return int(arch[:2])


def get_command(_menu, _option, _format="str"):
    """
    """
    general = get_section('General')
    language = get_config('General', 'language')
    suffix = "" if not bool(general.get('noconfirm')) else " --noconfirm"
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
        _app = get_alias(name_app, language)
        for pack in _app:
            commands.append(pack.split() if _format == "list" else pack)
    return commands


def show_menu(_menu):
    appearance = get_section('Appearance')
    language = get_config('General', 'language')
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


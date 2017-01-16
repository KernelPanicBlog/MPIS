#!/usr/bin/env python3
#-*- coding: utf-8 -*-
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
# _____________________________________________________________________________
from mpislib.traslate import tr
from mpislib.db import Database
from mpislib.resource import Resource
from mpislib.colorize import colorize
from mpislib.colorize import Estilo
# ----------------------------------------------------------------------
# Clases
# ----------------------------------------------------------------------


class Node:
    """ >>> """
    def __init__(self, _name, _parent=None):
        self.__name = _name
        self.__parent = _parent
        self.__childern = []

    @property
    def parent(self):
        """ >>> """
        return self.__parent

    @property
    def childern(self):
        """ >>> """
        return self.__childern

    @property
    def name(self):
        """ >>> """
        return self.__name

    def add_childern(self, child):
        """ >>> """
        if isinstance(child, str):
            self.__childern.append(Node(child, self.name))
        elif isinstance(child, Node):
            self.__childern.append(child)

    def __getitem__(self, _item):
        return self.__childern[_item]

    def __repr__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Menu:
    """ >>> """
    def __init__(self):
        self._resource = Resource()
        self._db = Database(self._resource.path_db())
        self.nodos = Node("root")
        self.nodos.add_childern(Node("Main Menu", self.nodos.name))
        self.__add_childern(self.nodos.childern[0])
        self._title_text_colour = None
        self._title_back_colour = None
        self._option_menu_colour = None
        self._user_input_colour = None
        self.load_appearance()

    def load_appearance(self):
        self._title_text_colour = self._db.get_config("title_text_colour")
        self._title_back_colour = self._db.get_config("title_back_colour")
        self._option_menu_colour = self._db.get_config("option_menu_colour")
        self._user_input_colour = self._db.get_config("user_input")

    def __add_childern(self, _node):
        """ >>> """
        childern = find_menu(_node.name)
        if childern is not None:
            for child in childern:
                if child[1]:
                    new_node = Node(child[0], _node.name)
                    _node.add_childern(new_node)
                    self.__add_childern(new_node)
                elif child[0] == "incategory":
                    data = self._db.get_category(_node.name)
                    d = {}
                    childern_to_add = [d.setdefault(x, x) for x in data if x not in d]
                    for h in childern_to_add:
                        _node.add_childern(h[0])
                else:
                    _node.add_childern(child[0])

    def show_menu(self, _menu, _tasks):

        option_bar = tr("back (b)") + "\t" + tr("help (h)")\
                     + "\t" + tr("exit (e)") + "\t"\
                     + (tr("Tasks (t)") if _tasks else "")

        # Title
        print(colorize.aplicar(Estilo.negrita.value,
                               self._title_text_colour,
                               self._title_back_colour)
              + tr(_menu.name) + colorize.reset() + "\n")

        # Options
        for item, index in zip(_menu.childern,
                               range(len(_menu.childern))):
            print(colorize.aplicar(Estilo.normal.value,
                                   self._option_menu_colour)
                  + "{0}) {1}".format(index, tr(str(item))) + colorize.reset())

        # Option bar
        print("\n" + colorize.aplicar(Estilo.negrita.value,
                               self._title_text_colour,
                               self._title_back_colour)
              + option_bar + colorize.reset())




# ----------------------------------------------------------------------
# Menu
# ----------------------------------------------------------------------

MENU = {
    "Main Menu": [
        ("Update System", True),
        ("Install applications", True),
        ("Uninstall applications", True),
        ("Install DEs and WMs", True),
        ("Uninstall DEs and WMs", True),
        ("Personalization", True),
        ("List packages installed", False),
        ("Settings ...", True),
        ("About", True)
    ],
    "Update System": [
        ("Refresh Mirrors and Keys", False),
        ("Pacman repositories update", False),
        ("AUR repositories update", False),
        ("Update all system", False),
        ("Update all system and refresh mirrors", False),
        ("Clear cache and orphan PACKAGES", False),
        ("See the content of mirrorlist file", False)
    ],
    "Install applications": [
        ("Office", True),
        ("Multimedia", True),
        ("Development", True),
        ("Internet", True),
        ("Games", True),
        ("System Tools", True)
    ],
    "Uninstall applications": [
        ("Office", True),
        ("Multimedia", True),
        ("Development", True),
        ("Internet", True),
        ("Games", True),
        ("System Tools", True)
    ],
    "Personalization": [
        ("Themes", True),
        ("iconos", True)
    ],
    "Install DEs and WMs": [
        ("DEs", True),
        ("WMs", True)
    ],
    "Uninstall DEs and WMs": [
        ("DEs", True),
        ("WMs", True)
    ],
    "About": [
        ("See README File", False),
        ("See CHANGELOG File", False),
        ("Report bug!", False),
        ("About MPIS", False),
    ],
    "Settings": [
        ("Toggle --noconfirm", False),
        ("Toggle multi-install", False),
        ("Appearance", False),
        ("Set language", False)
    ],
    "DEs": [
        ("incategory", False)
    ],
    "WMs": [
        ("incategory", False)
    ],
    "Office": [
        ("incategory", False)
    ],
    "Multimedia": [
        ("incategory", False)
    ],
    "Development": [
        ("incategory", False)
    ],
    "Internet": [
        ("incategory", False)
    ],
    "Games": [
        ("incategory", False)
    ],
    "System Tools": [
        ("incategory", False)
    ],
}
# ----------------------------------------------------------------------
# Funciones
# ----------------------------------------------------------------------


def find_menu(name_menu):

    global MENU

    return MENU.get(name_menu)

GlobalMenu = Menu()

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
# Menus
###############################################################################
# EN -> ingles

MENUS_EN = {
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
        ("About Mpis", False),
    ],
    "Settings ...": [
        ("Toggle --noconfirm", False),
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
###############################################################################
# ES - español

MENUS_ES = {
    "Menu principal": [
        ("Actualizar sistema", True),
        ("Instalar aplicaciones", True),
        ("Desinstalar aplicaciones", True),
        ("Instalar DEs and WMs", True),
        ("Desinstalar DEs and WMs", True),
        ("Personalizacion", True),
        ("Listar los paquetes instalados", False),
        ("Configuracion ...", True),
        ("Acerca", True)
    ],
    "Actualizar sistema": [
        ("Refrescar los espejos y las llaves", False),
        ("Actualizar los repertorios de pacman", False),
        ("Actualizar los repertorios de AUR", False),
        ("Actualizar todo el sistema", False),
        ("Actualizar todo el sistema y refrescar los espejos", False),
        ("Limpiar la cache y los paquetes huerfanos", False),
        ("Ver el contenido del archivo mirrorlist", False)
    ],
    "Instalar aplicaciones": [
        ("Oficina", True),
        ("Multimedia", True),
        ("Desarrollo", True),
        ("Internet", True),
        ("Juegos", True),
        ("Herramientas del sistema", True)
    ],
    "Desinstalar aplicaciones": [
        ("Oficina", True),
        ("Multimedia", True),
        ("Desarrollo", True),
        ("Internet", True),
        ("Juegos", True),
        ("Herramientas del sistema", True)
    ],
    "Personalizacion": [
        ("temas", True),
        ("iconos", True)
    ],
    "Instalar DEs and WMs": [
        ("DEs", True),
        ("WMs", True)
    ],
    "Desinstalar DEs and WMs": [
        ("DEs", True),
        ("WMs", True)
    ],
    "Acerca": [
        ("Ver el archivo README", False),
        ("Ver el archivo CHANGELOG", False),
        ("Reportar falla!", False),
        ("Acerca de Mpis", False),
    ],
    "Configuracion ...": [
        ("Conmutar --noconfirm", False),
        ("Apariencia", False),
        ("Establecer idioma", False)
    ],
    "DEs": [
        ("incategory", False)
    ],
    "WMs": [
        ("incategory", False)
    ],
    "Oficina": [
        ("incategory", False)
    ],
    "Multimedia": [
        ("incategory", False)
    ],
    "Desarrollo": [
        ("incategory", False)
    ],
    "Internet": [
        ("incategory", False)
    ],
    "Juegos": [
        ("incategory", False)
    ],
    "Herramientas del sistema": [
        ("incategory", False)
    ],
}
###############################################################################
# Funciones
###############################################################################


def find_menu(name_menu, lan):

    global MENUS_ES
    global MENUS_EN

    return MENUS_ES.get(name_menu) if lan == "es" else MENUS_EN.get(name_menu)

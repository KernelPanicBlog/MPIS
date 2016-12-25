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
from configparser import ConfigParser
from mpislib.resource import get_path_config

###############################################################################
# GLOBAL CONF
###############################################################################
CONFIG = ConfigParser()

###############################################################################
# Functions
###############################################################################


def read_config():
    global CONFIG

    if not CONFIG.read(get_path_config()):
        __set_default_config()

    return CONFIG


def __set_default_config():
    global CONFIG

    CONFIG['General'] = {
        'noconfirm': "True",
        'language': "en",
        'multi-install': "False"
        }
    CONFIG['Appearance'] = {
        'menu-title': "Highlighted",
        'option-menu': "Green",
        'user-input': "Green-2",
        'notifications': "Red"
        }
    with open(get_path_config(), "w") as config_file:
        CONFIG.write(config_file)


def save_config(_config):
    global CONFIG
    CONFIG = _config
    with open(get_path_config(), "w") as config_file:
        CONFIG.write(config_file)


def update_config(_section, _config, _val):
    global CONFIG

    CONFIG[_section][_config] = _val

    save_config(CONFIG)


def get_section(_section):
    global CONFIG

    return CONFIG[_section]


def get_config(_section, _config):
    global CONFIG

    return CONFIG[_section].get(_config)

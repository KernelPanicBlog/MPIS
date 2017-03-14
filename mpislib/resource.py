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
import os


class Resource:
    """ Class that provides the path of resource file. """
    def __init__(self):
        self.__path_home = os.getenv("HOME")
        self.__path_config = self.__path_home + "/.config/mpis"
        self.__path_file = "/usr/share/mpis"
        self.__path_tr = os.path.join(self.__path_config, "locale")
        self.__path_db = os.path.join(self.__path_config, "db")

    def path_tr_file(self):
        """ Returns the directory of the translation files. """
        return self.__path_tr

    def path_file(self, _name):
        """ Returns the directory of the files. """
        return os.path.join(self.__path_file, _name)

    def path_db(self):
        """ Returns the path of the database. """
        return os.path.join(self.__path_db, 'mpis.db')

    def path_home(self):
        """ Returns the HOME path. """
        return self.__path_home

    def path_db_restore(self):
        """ Returns the path of the database for the restore. """
        return os.path.join(self.__path_file, 'db/mpis.db')

    def path_tr_restore(self, _file):
        """ Returns the directory of the translation files
        for the restore. """
        return os.path.join(self.__path_file, "locale{}".format(_file))


GlobalResource = Resource()

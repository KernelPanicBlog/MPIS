#!/usr/bin/env python3
#-*- coding: utf-8 -*-
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
# _____________________________________________________________________________
import os
import csv
from mpislib.db import Database
from mpislib.resource import Resource


class Translate:
    """Class provided by the decorator to translate texts.

       example:
            @Translate
            def Translating_function(string)
                return string

            Translating_function("Hi")

       result:
            >> hola
    """
    def __init__(self, f):
        self.f = f
        self._resource = Resource()
        self._db = Database(self._resource.path_db())
        self.ext = ".tr"
        self.lang = self._db.get_config('language')
        self.dic_tr = None
        self.list_tr = None
        self.dic_tr, self.list_tr = self.__read_tr()

    def __call__(self, string):
        def wrapper(*args, **kw_args):
            """Wrapping function"""
            return self.f(self.__get_traduccion(*args, **kw_args))
        return wrapper(string)

    def __get_traduccion(self, _string):
        """Private function.
        Search in the translation dictionary, the string.
        Return the translation if found else returns the same string.
        """
        try:
            # Generates the key for the search of the translation.
            _key = "msg_" + str(self.list_tr.index(_string))
            tr_string = self.dic_tr.get(_key)
            return tr_string
        except ValueError:
            return _string

    def __read_tr(self):
        """Private function.
        Read the translation file, fill the dictionary and generate a list
        with the indexes for the searches.
        Return dict, list
        """
        dic = {}
        list_tr = []
        if not self.dic_tr:
            file_tr = os.path.join(self._resource.path_tr_file(),
                                   str(self.lang + self.ext))
            # Fill in the translation dictionary
            with open(file_tr, "r") as _file:
                trs = csv.reader(_file)
                for reg in trs:
                    dic[reg[0]] = reg[1]
            file_tr = os.path.join(self._resource.path_tr_file(),
                                   str("EN_us" + self.ext))
            # Generates the list of indexes for the searches
            with open(file_tr, "r") as _file:
                trs = csv.reader(_file)
                for reg in trs:
                    list_tr.append(reg[1])
        dic_return = dic if not self.dic_tr else self.dic_tr
        list_return = list_tr if not self.list_tr else self.list_tr
        return dic_return, list_return


@Translate
def tr(string):
    return string

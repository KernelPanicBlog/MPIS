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

import sqlite3


class Database:
    """ >>> """
    def __init__(self, name=None):

        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        """ >>> """
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()

        except sqlite3.Error:
            print("Error connecting to database!.")

    def close(self):
        """ >>> """
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def update_config(self, conf, value):
        table = 'config'

        query = 'UPDATE {0} SET value={2} WHERE name=\"{1}\"'
        query_sql = query.format(table, conf, value)

        self.cursor.execute(query_sql)
        self.conn.commit()

    def get_command(self, app, _install=True):
        """ >>> """
        rows = []
        table = 'packages'
        columns = 'repository, package, sequence'
        query = 'SELECT {0} from {1} WHERE name = \"{2}\" ORDER BY sequence'
        query_sql = query.format(columns, table, app)
        try:
            self.cursor.execute(query_sql)

            # fetch data
            data = self.cursor.fetchall()
            if data:
                for item in data:
                    if item[0] == "pacman":
                        arg = "-S " if _install else "-R "
                        rows.append("sudo pacman " + arg + item[1])
                    elif item[0] == "yaourt":
                        parm = self.get_config("noconfirm")
                        noconfirm = " --noconfirm" if parm == "True" else ""
                        arg = "-S " if _install else "-R "
                        rows.append("yaourt " + arg + item[1] + noconfirm)
            else:
                table = 'alias'
                columns = 'command'
                query = 'SELECT {0} from {1} WHERE name = \"{2}\"'
                query_sql = query.format(columns, table, app)
                self.cursor.execute(query_sql)

                # fetch data
                data = self.cursor.fetchall()
                for item in data:
                    rows.append(item[0])

        except sqlite3.OperationalError:
            print("Error connecting to database!.")
        return rows

    def get_config(self, _conf):
        table = 'config'
        columns = 'value'
        query = 'SELECT {0} from {1} WHERE name = \"{2}\"'
        query_sql = query.format(columns, table, _conf)
        self.cursor.execute(query_sql)

        # fetch data
        rows = self.cursor.fetchall()

        return rows[0][0]

    def get_category(self, _category):
        """ >>> """
        table = 'packages'
        columns = 'name, category'
        query = 'SELECT {0} from {1} WHERE category = \"{2}\"'
        query_sql = query.format(columns, table, _category)
        self.cursor.execute(query_sql)

        # fetch data
        rows = self.cursor.fetchall()

        return rows

    def search_packages(self):
        rows = []
        query = 'SELECT name from packages'
        try:
            self.cursor.execute(query)

            # fetch data
            data = self.cursor.fetchall()
            for item in data:
                rows.append(item[0])
            rows = list(set(rows))
        except sqlite3.OperationalError:
            print("Error connecting to database!.")

        return rows

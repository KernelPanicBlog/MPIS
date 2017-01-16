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
# ------------------------------------------------------------------------------
#   META DATA
# ------------------------------------------------------------------------------
__version__ = 2.0
__autores__ = """KernelPanicBlog team:
SniferL4bs  | https://www.sniferl4bs.com
NeoRanger   | https://www.neositelinux.com
Harrinsoft  | harrinsoft@gmail.com"""
# ------------------------------------------------------------------------------

from mpislib.resource import GlobalResource
import os.path as path

#
if not path.isfile(GlobalResource.path_db()):
    try:
        import subprocess
        dir = GlobalResource.path_home() + "/.config/mpis/db"
        cmd = "mkdir -p {0}".format(dir)
        subprocess.call(cmd.split())
        file = GlobalResource.path_db_restore()
        cmd = "cp {0} {1}".format(file, dir)
        subprocess.call(cmd.split())
    except Exception:
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)

if not path.isfile(GlobalResource.path_tr_file() + "/EN_us.tr"):
    try:
        import subprocess
        dir = GlobalResource.path_tr_file()
        cmd = "mkdir -p {0}".format(dir)
        subprocess.call(cmd.split())
        file = GlobalResource.path_tr_restore("/EN_us.tr")
        cmd = "cp {0} {1}".format(file, dir)
        subprocess.call(cmd.split())
    except Exception:
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)

if not path.isfile(GlobalResource.path_tr_file() + "/ES_es.tr"):
    try:
        import subprocess
        dir = GlobalResource.path_tr_file()
        cmd = "mkdir -p {0}".format(dir)
        subprocess.call(cmd.split())
        file = GlobalResource.path_tr_restore("/ES_es.tr")
        cmd = "cp {0} {1}".format(file, dir)
        subprocess.call(cmd.split())
    except Exception:
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)


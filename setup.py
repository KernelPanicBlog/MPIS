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
# install an application or config some tools and environments.
#
# MPIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS; If not, see <http://www.gnu.org/licenses/>.
#
# MPIS: Setup file
#

from distutils.core import setup


def get_readme():
    with open("README.rst") as readme:
        return readme.read()

setup(name="mpis",
      version="0.3.0-alpha1",
      description="This script allows to configure the system,"
                  "install some applications for a regular work day designed"
                  "for developers, gamers, musicians and more...",
      long_description=get_readme(),
      keywords="manjaro linux post install script",
      author="KernelPanicBlog Team",
      author_email="kernelpanicblog1@gmail.com",
      url="https://kernelpanicblog.wordpress.com",
      license="gplv3",
      packages=["mpislib"],
      data_files=[("/usr/lib/mpis", ["menu.xml"]),
                  ("/usr/share/licenses/mpis", ["LICENSE"]),
                  ("/usr/share/mpis", ["CHANGELOG.rst"])],
      scripts=["mpis"],)

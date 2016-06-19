#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MPIS: Setup file
#

from distutils.core import setup


def get_readme():
    with open("README.md") as readme:
        return readme.read()

setup(
      name="mpis",
      version="0.2a",
      description="This script allows to configure the system, install some applications" \
                  "for a regular work day thinked in developers, gamers, musicians and more...",
      long_description=get_readme(),
      keywords="manjaro linux post install script",
      author="KernelPanicBlog Team",
      author_email="kernelpanicblog1@gmail.com",
      url="https://kernelpanicblog.wordpress.com",
      license="gplv3",
      py_modules=["core.core"],
      data_files = [("/usr/lib/mpis", ["menu.xml"]),
                    ("/usr/share/licenses/mpis", ["LICENSE"])],
      scripts=["mpis"],
)


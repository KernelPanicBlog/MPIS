#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MPIS: Setup file
#

from distutils.core import setup

def get_readme(file):
    with open(file) as readme:
        return readme.read()

<<<<<<< HEAD
setup(name="mpis", version="unstable",
      description="This script allows to configure the system, install some applications" \
                  "for a regular work day thinked in developers, gamers, musicians and more...",
      long_description=get_readme(),
      keywords="manjaro linux post install script",
      author="KernelPanicBlog Team",
      url="https://kernelpanicblog.wordpress.com",
      license="gplv3",
      py_modules=["core.core"],
      scripts=["mpis"])
=======
setup(
      name              =    "mpis",
      version           =    "0.1a",
      description       =    "This script allows to configure the system, install some applications" \
                             "for a regular work day thinked in developers, gamers, musicians and more...",
      long_description  =    get_readme("README.md"),
      keywords          =    "manjaro linux post install script",
      author            =    "KernelPanicBlog Team",
      author_email      =    "kernelpanicblog1@gmail.com",
      url               =    "https://kernelpanicblog.wordpress.com",
      license           =    "gplv3",
      py_modules        =    ["core.core"],
      data_files        =    ["apps.config", "menus.config", "LICENSE", "README.md"],
      scripts           =    ["mpis"],
)
>>>>>>> c836f85e6b39fbef57708155a9c6d9ed8ef58b02

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Core for MPIS with YAML compatibility.
# Here will live the YAML reader for menus and the new menu logic (I will try to deprecate the menus.config file)
#

import os
import sys
import yaml
# Python 2/3 compatibility and make use of libYAML for faster YAML loading
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class MPIS:
    def ReadConfig(file):
        config_file = open(file, "r")
        with config_file:
            config_file = yaml.load(config_file, Loader=Loader)

    def GetSection():
        for section in config_file[0]:
            print(section)

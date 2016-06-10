#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Manjaro Post Installation Script (rewrite for YAML compatibility):
# It allows  users to choose different options such as
# install an application or config some tools and environments.

from core_yaml import MPIS

config = MPIS.ReadConfig("config.yml")
MPIS.GetConfig(config)

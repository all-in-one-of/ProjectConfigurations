#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  17:36
# Email     : spirit_az@foxmail.com
# File      : __init__.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import sys

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
dirname = os.path.dirname(__file__)
sys.path.insert(0, dirname)

os.environ['PATH'] += os.pathsep + dirname
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      : 2019/8/20 15:11
# Email     : spirit_az@foxmail.com
# File      : startHoudini.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os

import initShelves


# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class setup(object):
    def __init__(self, projectName):
        self.folder, self.proName = os.path.split(projectName)
        self.menuPro = os.path.join(self.folder, 'houdiniConf', 'shelf_%s' % self.proName).replace('\\', '/')
        pass

    def run(self):
        try:
            self.init_shelf()
        except:
            print('init shelf error')

    def init_shelf(self):
        shelf = initShelves.initShelves(self.menuPro)
        shelf.run()

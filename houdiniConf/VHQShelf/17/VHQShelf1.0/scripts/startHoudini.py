#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      : 2019/8/20 15:11
# Email     : spirit_az@foxmail.com
# File      : startHoudini.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import sys
import hou
import importlib

import initShelves
reload(initShelves)


# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class setup(object):
    def __init__(self, projectName):
        self.folder, self.proName = os.path.split(projectName)
        self.menuPro = os.path.join(self.folder, 'houdiniConf', 'shelf_%s' % self.proName).replace('\\', '/')

        self.folder in sys.path or sys.path.insert(0, self.folder)
        self.projectName = os.path.splitext(os.path.basename(projectName))[0]
        self.project = importlib.import_module(self.projectName)

    def run(self):
        self.init_Session()
        try:
            self.init_shelf()
        except:
            print('init shelf error')
        else:
            print('succeed : init shelf %s' % os.path.splitext(self.proName)[0])
        finally:
            pass

    def init_shelf(self):
        shelf = initShelves.initShelves(self.menuPro)
        shelf.run()

    def init_Session(self):
        HOUDINI_SESSION_PATH = self.project.HOUDINI_SESSION_PATH
        for(k, v) in HOUDINI_SESSION_PATH.items():
            hou.appendSessionModuleSource('{}="{}"'.format(k, v))


if __name__ == '__main__':
    # fire.Fire(setup)
    args = sys.argv[1:]
    setup(args[0]).run()
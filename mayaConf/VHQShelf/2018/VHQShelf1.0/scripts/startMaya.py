#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time         : 2018/12/13 20:05
# @email        : spirit_az@foxmail.com
# @fileName     : startMaya.py
__author__ = 'ChenLiang.Miao'

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
import os
import re
import sys
import importlib
import maya.cmds as cmds
import maya.mel as mel


# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
class setup(object):
    def __init__(self, proName):
        super(setup, self).__init__()
        self.projectName = os.path.splitext(os.path.basename(proName))[0]
        folder, f = os.path.split(proName)
        self.menuPro = os.path.join(folder, 'mayaConf').replace('\\', '/')
        self.menuF = 'menu_%s' % self.projectName
        self.project = importlib.import_module(self.projectName)  # imp.load_source('project', proName)
        self.toolsEnv = self.project.MAYAToolVariables
        self.init_env()
        self.init_plugs()
        self.init_menu()

    def init_env(self):
        for (k, v) in self.toolsEnv.items():
            if not v:
                continue

            for each in v:
                if each not in mel.eval('getenv "{0}"'.format(k)).split(';'):
                    mel.eval('putenv "{0}" (`getenv "{0}"`+";"+"'.format(k) + each + '")')

    def init_plugs(self):
        for plug in self.project.MAYAPluginList:
            if cmds.pluginInfo(plug, q=1, l=1):
                continue
            try:
                cmds.loadPlugin("{}".format(plug))
            except:
                pass

    def init_menu(self):
        self.menuPro in sys.path or sys.path.insert(0, self.menuPro)
        menuP = __import__(self.menuF)
        menuP.run()


def run(projectName):
    # folder = cmds.getModulePath(moduleName='MCLShelf')
    # dirF = os.path.basename(folder)
    # modPath = os.path.join(folder, "%s.mod" % dirF).replace('\\', '/')
    # if not os.path.isfile(modPath):
    #     return
    # with open(modPath) as f:
    #     prog = re.compile('TOOLS_CONFIGURATION_PATH.=.*')
    #     folder = prog.findall(f.read())
    #     if not folder:
    #         return
    #     else:
    #         folderDir = folder[0].split('=')[-1].strip()
    #
    # if not folderDir:
    #     return
    #
    # projectPath = os.path.normpath(os.path.join(folderDir, '%s.py' % projectName))
    setup(projectName)

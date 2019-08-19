#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import sys

import maya.OpenMaya as om
import maya.OpenMayaMPx as ompx

import shelf_Scripts
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import startMaya

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
kPluginCmdName = 'projectConf'
projectFlag = '-lp'
projectFlagLong = '-loadProject'
shelfFlag = '-ls'
shelfFlagLong = '-loadShelf'

authorMessage = """
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
author  : ChenLiang.Miao
email   : spirit_az@foxmail.com
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class ProjectConf(ompx.MPxCommand):
    def __init__(self):
        super(ProjectConf, self).__init__()
        self.project = None

    def doIt(self, args):
        argdb = om.MArgParser(self.syntax(), args)

        if argdb.isFlagSet(shelfFlag):
            # s = ['MOD', 'RIG', 'SDR', 'TRK', 'LAY', 'ANI', 'EFX', 'CFX', 'LGT', 'ENV']
            shelfFlagTst = argdb.flagArgumentString(shelfFlag, 0)
            if shelfFlagTst == 'all':
                shelf_Scripts.create_shelf()
            elif shelfFlagTst == 'remove':
                shelf_Scripts.create_shelf(remove=1)
            else:
                shelf_Scripts.create_shelf(False, shelfFlagTst)

        if argdb.isFlagSet(projectFlag):
            project = argdb.flagArgumentString(projectFlag, 0)
            if not project:
                raise ValueError('No import project name!!!')

            else:
                startMaya.run(project)

def cmdCreator():
    return ProjectConf()


def syntaxCreator():
    syntax = om.MSyntax()
    syntax.addFlag(projectFlag, projectFlagLong, om.MSyntax.kString)
    syntax.addFlag(shelfFlag, shelfFlagLong, om.MSyntax.kString)
    return syntax


def initializePlugin(plugin):
    om.MGlobal_displayInfo(authorMessage)
    pluginFn = ompx.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(kPluginCmdName, cmdCreator, syntaxCreator)
    except:
        sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
        raise


def uninitializePlugin(plugin):
    pluginFn = ompx.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(kPluginCmdName)
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % kPluginCmdName
        )
        raise

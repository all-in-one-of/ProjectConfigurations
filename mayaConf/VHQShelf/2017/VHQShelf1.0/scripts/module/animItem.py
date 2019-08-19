#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/6/13 16:30
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import maya.cmds as cmds
import maya.mel as mel
import __init__


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class addItem(__init__.add_item):
    def __init__(self, *args):
        if not args.__len__():
            raise KeyError("Must be enter parent tableLayer!!!")
        super(addItem, self).__init__(args[0])
        self.run()

    def run(self):
        super(addItem, self).run()
        cmds.menuItem(l='change plane', c='from GNR.PlaneEdit import animation;reload(animation);animation.run()', p=self.popupMenu)
        cmds.menuItem(l='bake camera', c="mel.eval('source \"scripts/melBakeCAm.mel\";rcExport2AE;')", p=self.popupMenu)
        cmds.menuItem(l='change assembly', c='from LAY.scripts import assemblyChanged;reload(assemblyChanged);'
                                             'assemblyChanged.changeBySel()', p=self.popupMenu)
        cmds.menuItem(l='vp20 preview', c='from ANI.VP20Preview import openUI;reload(openUI);openUI.door()', p=self.popupMenu)
        cmds.menuItem(l='help', i='cloud_download.png', c='print "This is animation tools"', p=self.popupMenu)

        cmds.setParent('..', m=True)
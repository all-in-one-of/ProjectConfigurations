#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/6/13 16:30
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import maya.cmds as cmds
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
        cmds.menuItem(l='Lighting tool', c='import generic; generic.lightTool()', p=self.popupMenu)
        cmds.menuItem(l='change plane', c='from GNR.PlaneEdit import lighting;reload(lighting);lighting.run()',
                      p=self.popupMenu)
        cmds.menuItem(l='change assembly', c='from LAY.scripts import assemblyChanged;reload(assemblyChanged);'
                                             'assemblyChanged.changeBySel()', p=self.popupMenu)
        cmds.menuItem(l='help', i='cloud_download.png', c='print "This is lighting tools"', p=self.popupMenu)
        cmds.menuItem(l='alembic mtl', c='from LGT.scripts import alembic_mtl\n'
                                         'amtl = alembic_mtl.AssignMtlCtl()\n'
                                         'amtl.selectAllCtl()',
                      p=self.popupMenu)

        cmds.menuItem(l='build crowd (temp)', c='from CGTmW.Pipeline_tools.module.shot.crowd import abcToMa;'
                                                 'reload(abcToMa);abcToMa.run()',
                      p=self.popupMenu)

        cmds.menuItem(l='assign crowd shader', c='from CGTmW.Pipeline_tools.module.shot.crowd import importMaterial;'
                                                 'reload(importMaterial);importMaterial.run()',
                      p=self.popupMenu)

        cmds.setParent('..', m=True)

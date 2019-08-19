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
        cmds.menuItem(l='braid', c='from MOD.JUM import braid;braid.run()', p=self.popupMenu)
        cmds.menuItem(l='Mesh Resizer', c='from MOD.scripts import ResizeMesh;ResizeMesh.show()', p=self.popupMenu)
        cmds.menuItem(l='Dual Mesh', c="cmds.voronoiGen()", p=self.popupMenu)
        cmds.menuItem(l='AMT Normals LT', c="mel.eval('source \"MOD/AMTNormalsLT/AMTNormalsLT.mel\";')",
                      p=self.popupMenu)
        cmds.menuItem(l='AMT Mesh Blend', c="mel.eval('source \"MOD/Mesh_Blend1.2/AMT Mesh Blend/MeshBlend.mel\";')",
                      p=self.popupMenu)
        cmds.menuItem(l='Crease Plus', c="mel.eval('source \"MOD/CreasePlus/CreasePlus.mel\";')", p=self.popupMenu)
        cmds.menuItem(l='Mod It 2.0', c="from MOD.ModIt_2 import ModIt_2017;reload(ModIt_2017);ModIt_2017.run()", p=self.popupMenu)

        cmds.menuItem(divider=1, dividerLabel="Quick Pipe",  p=self.popupMenu)
        cmds.menuItem(l="Launch Quick Pipe",
                      c="mel.eval('source \"MOD/QuickPipe/LaunchQuickPipe.mel\";')",p=self.popupMenu)
        cmds.menuItem(l="Quick Pipe User Menu",
                      c="mel.eval('source \"MOD/QuickPipe/QuickPipeUserMenu.mel\";')", p=self.popupMenu)
        cmds.menuItem(divider=1, dividerLabel="----------",  p=self.popupMenu)
        cmds.menuItem(l='help', i='cloud_download.png', c='print "This is model tools"', p=self.popupMenu)

        cmds.setParent('..', m=True)

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
        cmds.menuItem(l='Add Follicle To Vertex', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/addFollicleToVertex.mel\";')")
        cmds.menuItem(l='Create Ribbon Controller', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/createRibbonController.mel\";')")

        cmds.menuItem(l='Create Joint On Curve 1', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/createJointOnCurve1.mel\"')")
        cmds.menuItem(l='Create Joint On Curve 2', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/createJointOnCurve2.mel\"')")
        cmds.menuItem(l='Create Joint On Curve 3', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/createJointOnCurve3.mel\"')")
        cmds.menuItem(l='Paint Deform', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('source \"scripts/DPK_paintDeform.mel\" ;DPK_paintDeform ;')")
        cmds.menuItem(l='jlCollisionDeformer', p=self.popupMenu,
                      c="import maya.mel as mel ;mel.eval('jlCollisionDeformer()')")

        cmds.menuItem(l='SoftClusterEX', p=self.popupMenu,
                      c="import SoftClusterEX;reload(SoftClusterEX);SoftClusterEX.launch()")

        cmds.menuItem(l='help', i='cloud_download.png', c='print "This is rig tools"', p=self.popupMenu)
        cmds.setParent('..', m=True)

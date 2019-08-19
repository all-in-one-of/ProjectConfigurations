#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/6/13 16:31
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import maya.cmds as cmds


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class add_item(object):
    def __init__(self, parent=None):
        self.parent = parent

    def run(self):
        self.popupMenu = cmds.popupMenu(p=self.parent, button = 1)
        # cmds.setParent(popupMenu, m=True)

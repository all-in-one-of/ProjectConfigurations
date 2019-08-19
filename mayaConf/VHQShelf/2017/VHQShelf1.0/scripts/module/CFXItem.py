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
        cmds.menuItem(l='Set Qualoth', c='from VFX.scripts import setQualoth;reload(setQualoth);setQualoth.main()',
                      p=self.popupMenu)
        cmds.menuItem(l='staggerFrame', c='from VFX.staggerFrame import openUI;reload(openUI);openUI.show()',
                      p=self.popupMenu)

        cmds.menuItem(l='set Yeti Cache', c='from VFX.setYetiCache import openUI;reload(openUI);openUI.show()',
                      p=self.popupMenu)

        cmds.menuItem(l='freld Direction', c='from VFX.freldDirection import openUI;reload(openUI);openUI.show()',
                      p=self.popupMenu)

        cmds.menuItem(l='timpWarp to anim', c='from VFX.timpWarp2anim import timp_warp_2_anim;reload(timp_warp_2_anim);timp_warp_2_anim.time_warp2anim()',
                      p=self.popupMenu)

        cmds.menuItem(l='help', i='cloud_download.png', c='print "This is CFX tools"', p=self.popupMenu)

        cmds.setParent('..', m=True)



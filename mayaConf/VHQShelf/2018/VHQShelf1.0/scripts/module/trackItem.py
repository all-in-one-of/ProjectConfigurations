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

        myMenu = cmds.menuItem(p=self.popupMenu, subMenu=True, to=True, l="VHQ Retimer")

        retimeCreateCommand = "import VHQTimeWrap;reload(VHQTimeWrap);VHQTimeWrap.create()"
        retimeCreateOptionCommand = "import create;reload(create);create.UI()"
        retimeClearCommand = "import VHQTimeWrap;reload(VHQTimeWrap);VHQTimeWrap.remove()"
        retimeReplaceCommand = "import VHQTimeWrap;reload(VHQTimeWrap);VHQTimeWrap.replaceBySel()"
        retimeBackCommand = "import VHQTimeWrap;reload(VHQTimeWrap);VHQTimeWrap.bakeAnimation()"

        cmds.menuItem(p=myMenu, divider=1, dividerLabel='initialize')
        # create retime file node
        cmds.menuItem(p=myMenu,
                      l="Retime Create...",
                      ann="create retime file node",
                      echoCommand=1,
                      c=retimeCreateCommand)
        cmds.menuItem(p=myMenu,
                      optionBox=True,
                      l="Retime Create Option Box...",
                      ann="create retime file node option box",
                      c=retimeCreateOptionCommand
                      )

        cmds.menuItem(p=myMenu,
                      l="Retime Clear...",
                      ann="delete all retime node",
                      c=retimeClearCommand
                      )

        cmds.menuItem(divider=1, dividerLabel="setting")
        cmds.menuItem(l="Replace Image Plane...",
                      ann="init replace image plane",
                      c=retimeReplaceCommand
                      )
        cmds.menuItem(p=myMenu,
                      l="Retime Enable...",
                      checkBox=True,
                      ann="Enable all retime node",
                      c=retimeEnableCommand
                      )

        cmds.menuItem(p=myMenu,
                      l="Retime bake...",
                      ann="bake into a new animation",
                      c=retimeBackCommand
                      )

        cmds.menuItem(l='Bake Locators Animation Data',
                      c="import TRC.scripts.bakeLocators as bakeLocators ;"
                        "reload(bakeLocators);bakeLocators.bakeLocators()",
                      p=self.popupMenu)

        cmds.setParent('..', m=True)


def retimeEnableCommand(conf):
    try:
        import VHQTimeWrap
    except ImportError:
        print "Please update your tools"
    else:
        VHQTimeWrap.setEnable(conf)

#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/6/13 14:39
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import imp
import os
import maya.cmds as cmds

from maya import mel

from module import animItem, CFXItem, effectItem, envItem, layoutItem
from  module import lgtItem, modelItem, rigItem, shaderItem, trackItem
for mo in [animItem, CFXItem, effectItem, envItem, layoutItem, lgtItem, modelItem, rigItem, shaderItem, trackItem]:
    reload(mo)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
__start_path__ = os.path.dirname(__file__)
env = imp.load_source('env', os.path.join(__start_path__, 'shelf_env.txt'))


def get_icon(image_f):
    base_icons = os.path.join(os.path.dirname(__start_path__), 'icons', image_f).replace('\\', '/')
    return base_icons


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class create_shelf(object):
    shelf_h = 32
    shelf_name = env.shelf_name

    def __init__(self, remove=False, *args):
        self.dictItem = {'MOD': [env.model_name, modelItem.addItem],
                         'RIG': [env.rig_name, rigItem.addItem],
                         'SDR': [env.shader_name, shaderItem.addItem],
                         'TRK': [env.track_name, trackItem.addItem],
                         'LAY': [env.layout_name, layoutItem.addItem],
                         'ANI': [env.anim_name, animItem.addItem],
                         'EFX': [env.effect_name, effectItem.addItem],
                         'CFX': [env.cfx_name, CFXItem.addItem],
                         'LGT': [env.light_name, lgtItem.addItem],
                         'ENV': [env.env_name, envItem.addItem]
                         }
        if remove:
            self.delete_shelf()
            return

        if not args:
            self.init_shelf()
            self.init_model(*self.dictItem)
        else:
            self.init_model(*args)

    @property
    def shelfName(self):
        return self.shelf_name

    @shelfName.setter
    def shelfName(self, name):
        self.shelf_name = name

    @shelfName.getter
    def shelfName(self):
        return self.shelf_name

    def init_shelf(self):
        self.delete_shelf()
        mel.eval('addNewShelfTab("{}")'.format(self.shelf_name))

    def delete_shelf(self):
        shelf_dir = cmds.internalVar(userShelfDir=True).split(';')
        for each in shelf_dir:
            file_path = os.path.join(each, 'shelf_{}.mel'.format(self.shelf_name))
            if os.path.exists(file_path):
                os.remove(file_path)
        tab_lay = mel.eval('string $temp = $gShelfTopLevel;')
        shelves = cmds.tabLayout(tab_lay, q=True, ca=True)
        if self.shelf_name in shelves:
            cmds.deleteUI('{0}|{1}'.format(tab_lay, self.shelf_name), layout=True)
            mel.eval('shelfTabChange();')

    def init_model(self, *args):
        for each in args:
            if not self.dictItem.has_key(each):
                return

            (selfButtonName, image_path), func = self.dictItem[each]
            self.update_shelfButton(selfButtonName, image_path, func)

    def update_shelfButton(self, selfButtonName, image_path, func):
        self.conf_shelfButton(image_path)
        pythonTxt = 'from scripts import shelf_Scripts\nreload(shelf_Scripts)\nshelf_Scripts.create_shelf(0, "{}")'.format(
            selfButtonName)
        selfButtonName = cmds.shelfButton(p=self.shelf_name,
                                          rpt=True,
                                          i1=image_path,
                                          sourceType="python",
                                          doubleClickCommand=pythonTxt,
                                          annotation=selfButtonName,
                                          width=3 * self.shelf_h,
                                          height=self.shelf_h
                                          )
        func(selfButtonName)
        mel.eval('shelfTabChange();')

    def conf_shelfButton(self, image_path):
        all_bt = cmds.shelfLayout(self.shelfName, q=True, childArray=True) or list()
        for each in all_bt:
            c_image_path = cmds.shelfButton(each, q=True, i=True)
            if image_path == c_image_path:
                delTxt = "deleteUI -control {};shelfTabRefresh;".format(each)
                mel.eval(delTxt)

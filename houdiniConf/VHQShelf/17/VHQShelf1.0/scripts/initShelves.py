#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      : 2019/8/20 16:13
# Email     : spirit_az@foxmail.com
# File      : initShelves.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import hou
import tempfile
import os
import sys
import importlib
import toolKeysEnv


# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class initShelves(object):
    def __init__(self, shelfPath):
        self.folder, filename = os.path.split(shelfPath)
        self.shelfName = os.path.splitext(filename)[0]

        self.folder in sys.path or sys.path.insert(0, self.folder)
        self.shelf_project = importlib.import_module(self.shelfName)

    def run(self):
        try:
            self._initShelves()
        except:
            print('something is error when it create shelf')

        finally:
            sys.path.remove(self.folder)

    def _initShelves(self):

        """kong
        添加自定义工具架
        :return:
        """
        # 如果已经找到的话，就删除掉，然后重新创建
        allShelves = hou.shelves.shelves()  # type:dict()
        for each in self.getAllPipelineName():
            houShelves = allShelves.get(each, None)
            houShelves and houShelves.destroy()
        # rebuild shelves

        for each in self.shelf_project.SHELVES_TABLES:
            self.create_shelf(each)

    def create_shelf(self, messageDic):
        """
        创建项目自定义工具架
        :param messageDic:
        :return:
        """
        shelfName = messageDic.get('name')
        shelfLabel = messageDic.get('label')
        shelfPath = os.path.join(tempfile.gettempdir(), '%s.shelf' % shelfLabel).replace('\\', '/')
        shelfNode = hou.shelves.newShelf(shelfPath, shelfName, shelfLabel)

        tools = messageDic.get('tools')
        for (toolName, toolLabel, toolCommand, toolLanguage, toolIcon) in tools:
            self.create_tools_on_shelf(shelfNode, toolName, toolLabel, toolCommand, toolLanguage, toolIcon)

    def create_tools_on_shelf(self, shelf, toolName, toolLabel, toolCommand, toolLanguage, toolIcon):
        """
        自定义工具架上的工具
        :param shelf:
        :param toolName:
        :param toolLabel:
        :param toolCommand:
        :param toolLanguage:
        :param toolIcon:
        :return:
        """
        toolLanguage = toolKeysEnv.toolsLanguage.get(toolLanguage)
        selfName = shelf.name()
        filePath = os.path.join(tempfile.gettempdir(), selfName, '%s.shelf' % toolLabel).replace('\\', '/')
        shelf.newTool(filePath, toolName, toolLabel, toolCommand, toolLanguage, toolIcon)

    def getAllPipelineName(self):
        """
        得到所有流程工具名称
        :return:
        """
        for each in self.shelf_project.SHELVES_TABLES:
            yield each.get('name')

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      : 2019/9/12 16:35
# Email     : spirit_az@foxmail.com
# File      : initMainMenu.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import hou

try:
    from xml.etree import cElementTree as eTree
except ImportError:
    from xml.etree import ElementTree as eTree


# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class initMainMenu(object):

    def __init__(self, mainMenuPath):
        self.menuPath = mainMenuPath

    def createMenu(self, xmlPath):
        if hou.applicationVersion()[0] >= 15:
            self._createDynMenu(xmlPath)

        else:
            self._createStcMenu(xmlPath)

    def _createDynMenu(self, xmlPath):
        pass

    def _createStcMenu(self, xmlPath):
        pass

    def _buileVHQMenu(self):
        root = eTree.Element('mainMenu')
        menubar = eTree.SubElement(root, 'menuBar')

    def _menuItem(self):
        pass

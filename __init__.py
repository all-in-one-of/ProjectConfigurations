#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  17:36
# Email     : spirit_az@foxmail.com
# File      : __init__.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import inspect
import os
import sys


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def getParentClasses(obj):
    """
    Get object's all of parent class...
    """
    if type(obj) == type:
        return inspect.getmro(obj)
    else:
        return inspect.getmro(obj.__class__)


def getFile(module, basename=True):
    if not basename:
        return module
    return os.path.splitext(os.path.basename(module))[0]


def getModulesPath(module):
    """
    return dir for imported module..
    """
    moduleFile = inspect.getfile(module)
    modulePath = os.path.dirname(moduleFile)
    return modulePath


def getScriptPath():
    """
    return dir path for used script..
    """
    scriptPath = getModulesPath(inspect.currentframe().f_back)
    return scriptPath


def getDirPath():
    return os.path.dirname(getScriptPath())


dirname = getDirPath()
sys.path.insert(0, dirname)

os.environ['PATH'] += os.pathsep + dirname

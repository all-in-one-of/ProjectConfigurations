#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  12:08
# Email     : spirit_az@foxmail.com
# File      : maya2014.py
__author__ = 'ChenLiang.Miao'

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
import scriptTool

FILENAME = scriptTool.getFile(__file__)
basePath = scriptTool.getDirPath().replace('\\', '/')
# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
ProjectName = ""
PipelineSoftware = ''
Softwares = ['MAYA', 'HOUDINI', 'SUBSTANCEPANTER', 'PHOTOSHOP']

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
FPS = 25
UNIT = 'cm'
Renderer = 'arnold5.3'

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
MAYA_VERSION = 2014
MAYAMenu = [{'General': {}},
            {'Model': [['scene optimize', 'from GNL.Check import openUI;reload(openUI);openUI.show(1, "Model")'],

                       ]},
            {'LookDiv': {}},
            {'Rigging': {}},
            {'CFX': {}},
            {'EFX': {}},
            {'Track': {}},
            {'Layout': {}},
            {'Animate': {}},
            {'Environment': {}},
            {'Lighting': {}},
            {'Help': {}}]

MAYAPluginList = ['AbcExport.mll', 'AbcImport.mll', 'matrixNodes.mll', 'gpuCache.mll', 'SHAPESBrush.mll',
                  'mtoa.mll', 'pgYetiMaya.mll', 'lookdevKit.mll', 'curveWarp.mll', 'modelingTookit.mll',
                  'fbxmaya.mll', 'objExport.mll', 'cgfxShader.mll', 'dx11Shader.mll', 'dgProfiler.mll',
                  'deformerEvaluator.mll', 'nearestPointOnMesh.mll', 'SOuP.mll',
                  'invertShape.mll', 'poseInterpolator.mll', 'projectConfiguration.py']

MAYAToolVariables = {
    'MAYA_SCRIPT_PATH': ['{}/Maya/Tools'.format(basePath),
                         '{}/Maya/Tools/ANI'.format(basePath),
                         '{}/Maya/Tools/CFX'.format(basePath),
                         '{}/Maya/Tools/EFX'.format(basePath),
                         '{}/Maya/Tools/ENV'.format(basePath),
                         '{}/Maya/Tools/GNL'.format(basePath),
                         '{}/Maya/Tools/LAY'.format(basePath),
                         '{}/Maya/Tools/LDV'.format(basePath),
                         '{}/Maya/Tools/LGT'.format(basePath),
                         '{}/Maya/Tools/MOD'.format(basePath),
                         '{}/Maya/Tools/RIG'.format(basePath),
                         '{}/Maya/Tools/TRK'.format(basePath),

                         ],
    'MAYA_PLUG_IN_PATH': [],
    'MAYA_SHELF_PATH': []
}

MAYA_BAT_PATH = {"MAYA_MODULE_PATH": ["{}/Maya/modules/MCLShelf/MCLShelf1.0".format(basePath),
                                      "{}/Maya/modules/SHAPESBrush/2014/SHAPESBrush1.0".format(basePath),
                                      "{}/Maya/modules/TheSetupMachine/TSM3".format(basePath),
                                      "{}/Maya/modules/MCLRig/MCLRig1.0".format(basePath),
                                      "{}/Maya/modules/retarget".format(basePath),
                                      "{}/Maya/modules/SOUP/2014/soup".format(basePath),
                                      "{}/Maya/modules/zMappedWrapDeformer".format(basePath),
                                      ],
                 'PYTHONPATH': [scriptTool.getScriptPath(),
                                '{}/Maya/Python/2.7/Lib/site-packages'.format(basePath),
                                '{}/Maya/Tools'.format(basePath),
                                '{}/Maya/Scritps'.format(basePath)],

                 }
MAYA_LOCATION = """
"D:/Program Files/Autodesk/Maya{0}/bin/maya.exe" -noAutoloadPlugins -command "loadPlugin //"projectConfiguration.py//";projectConf -ls all -lp //"{1}//";"
""".format(MAYA_VERSION, FILENAME)

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
HOUDINI_VERSION = "17.0.416"
HOUDINIMenu = [{'General': {}},
               {'Help': {}}]

HOUDINIToolVariables = {
}

HOUDINI_BAT_PATH = {}
HOUDINI_LOCATION = """
"D:/Program Files/Side Effects Software/Houdini {0}/bin/houdinifx.exe"
""".format(HOUDINI_VERSION)

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
SUBSTANCE_VERSION = ''

SUBSTANCE_BAT_PATH = {}

SUBSTANCE_LOCATION = """
"D:/Program Files/Allegorithmic/Substance Painter/Substance Painter.exe"
"""

#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time         : 2018/12/9 20:32
# @email        : spirit_az@foxmail.com
# @fileName     : 1001_PN_TD.py

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
import os
import scriptTool
FILENAME = scriptTool.getFile(__file__)
basePath = scriptTool.getDirPath().replace('\\', '/')

# FILENAME = "1001_PN_TD"
# basePath = '//192.168.0.50/Pipeline/ProjectConfigurations/ProjectConfigurations3.5'
# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
ProjectName = ""
PipelineSoftware = ''
PIPELINE_SOFTWARE = 'mantis'
Softwares = ['MAYA', 'HOUDINI', 'SUBSTANCEPANTER', 'PHOTOSHOP']

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
FPS = 24
UNIT = 'cm'
Renderer = 'arnold5.3'

# clarisse ---+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
CLARISSE_VERSION = 4.0

CLARISSE_BAT_PATH = {}

CLARISSE_LOCATION = """
"C:/Program Files/Isotropix/Clarisse iFX {}/Clarisse/clarisse.exe"
""".format(CLARISSE_VERSION)

# hiero -+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
HIERO_VERSION = '10.5'
hiero_v = 'v2'

HIERO_BAT_PATH = {}

HIERO_LOCATION = """
"C:/Program Files/Nuke{0}{1}/Nuke{0}.exe" --hiero
""".format(HIERO_VERSION, hiero_v)

# houdini ----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
HOUDINI_VERSION = "17.5.173"

HOUDINI_BAT_PATH = dict(HOUDINI_NVIDIA_OPTIX_DSO_PATH=['C:/Program Files/Side Effects Software/Houdini {0}/NVIDIA_OptiX'.format(HOUDINI_VERSION)],
	HOUDINI_OTLSCAN_PATH=['"','&', os.path.dirname(basePath) + '/Houdini/HDA_Libs/otls']
)

HOUDINI_RENDER_DRIVER = "R:"

HOUDINI_CACHE_DRIVER = "S:"

HOUDINI_LOCATION = '"C:/Program Files/Side Effects Software/Houdini {0}/bin/houdini.exe" -foreground "{1}/houdiniConf/houdini_project_config.py" {2}/Houdini {3} {4} {5} {6} waitforui "{1}/houdiniConf/SetShelf.py" {4}'.format(HOUDINI_VERSION, basePath, os.path.dirname(basePath), PIPELINE_SOFTWARE, FILENAME, HOUDINI_CACHE_DRIVER, HOUDINI_RENDER_DRIVER)

# maya --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
MAYA_VERSION = 2017
MAYAPluginList = ['AbcExport.mll', 'AbcImport.mll', 'matrixNodes.mll', 'gpuCache.mll', 'SHAPESBrush.mll',
                  'mtoa.mll', 'pgYetiMaya.mll', 'lookdevKit.mll', 'curveWarp.mll', 'modelingTookit.mll',
                  'fbxmaya.mll', 'objExport.mll', 'cgfxShader.mll', 'dx11Shader.mll', 'dgProfiler.mll',
                  'deformerEvaluator.mll', 'nearestPointOnMesh.mll',
                  'invertShape.mll', 'poseInterpolator.mll', 'projectConfiguration.py']
PROJECT_MAYA_PATH = os.path.dirname(basePath).replace('\\', '/')
REDSHIFT_CONF = {
    "REDSHIFT_COREDATAPATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_PLUG_IN_PATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/2017/nt-x86-64".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_SCRIPT_PATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/Common/scripts".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_XBMLANGPATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/Common/icons".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_RENDER_DESC_PATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/Common/rendererDesc".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_CUSTOM_TEMPLATE_PATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/Common/scripts/NETemplates".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_MAYAEXTENSIONSPATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Plugins/Maya/2017/nt-x86-64/extensions;{0}/Maya/modules/Yeti/{1}/Yeti2.2.5/plug-ins".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_PROCEDURALSPATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Procedurals".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_LICENSEPATH": "{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/lic".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),

}

MAYAToolVariables = {
    'MAYA_SCRIPT_PATH': ['{0}/Maya/Tools/{1}'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/ANI'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/CFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/CGTmW'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/EFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/ENV'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/GNR'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/LAY'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/LGT'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/MOD'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/REDS'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/RIG'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/SUR'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/TRC'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/VFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),

                         ],
    'MAYA_PLUG_IN_PATH': []
}

MAYA_BAT_PATH = dict(XBMLANGPATH=['{0}/Maya/icons/{1}'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                  REDSHIFT_CONF['REDSHIFT_XBMLANGPATH']
                                  ],
                     MAYA_DISABLE_CER=1,
                     MAYA_DISABLE_CLIC_IPM=1,
                     MAYA_UI_LANGUAGE='en_US',
                     MAYA_MODULE_PATH=["{0}/mayaConf/VHQShelf/{1}/VHQShelf1.0".format(basePath, MAYA_VERSION),
                                       "{0}/Maya/modules/Yeti/{1}/Yeti2.2.5".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/Miarmy/{1}/Miarmy6.7.11".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/SoftClusterEX/{1}/SoftClusterEX1.0".format(
                                           PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/mtoa/{1}/mtoa2.1.0".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/SHAPESBrush/{1}/SHAPESBrush1.0".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/TheSetupMachine/{1}/TSM3".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/Qualoth/{1}/Qualoth4.2.8".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/realflow/{1}/reaflow6.0.1.1".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/hardmesh/{1}/hardmesh_2.2.1".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/Ziva/{1}/ZivaVFX1.6".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/UVLayout/{1}/UVLayout".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/SOuP/{1}/soup".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                       "{0}/Maya/modules/mgear/{1}/mgear_3.1.1".format(PROJECT_MAYA_PATH, MAYA_VERSION),

                                       ],
                     PYTHONPATH=[os.path.dirname(__file__).replace('\\', '/'),
                                 '{0}/Maya/Python/{1}/Lib/site-packages'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                 '{0}/Maya/Tools/{1}'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                 '{0}/Maya/Scritps/{1}'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                 REDSHIFT_CONF['REDSHIFT_SCRIPT_PATH']

                                 ],
                     MAYA_SHELF_PATH=["{0}/Maya/modules/UVLayout/{1}/UVLayout/shelves".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                      "{0}/Maya/modules/SOuP/{1}/soup/shelves".format(PROJECT_MAYA_PATH, MAYA_VERSION),
                                      # "C:/Program Files/RedPack/maya/MayaPreferences/2017/prefs/shelves"],
                                      ],
                     PATH=['{}/bin'.format(REDSHIFT_CONF['REDSHIFT_COREDATAPATH'])],
                     MAYA_SCRIPT_PATH=[REDSHIFT_CONF['REDSHIFT_SCRIPT_PATH']],
                     MAYA_PLUG_IN_PATH=[REDSHIFT_CONF['REDSHIFT_PLUG_IN_PATH']],
                     MAYA_RENDER_DESC_PATH=[REDSHIFT_CONF['REDSHIFT_RENDER_DESC_PATH']],
                     MAYA_CUSTOM_TEMPLATE_PATH=[REDSHIFT_CONF['REDSHIFT_CUSTOM_TEMPLATE_PATH']],
                     REDSHIFT_MAYAEXTENSIONSPATH=[REDSHIFT_CONF['REDSHIFT_MAYAEXTENSIONSPATH']],
                     REDSHIFT_PROCEDURALSPATH=["{0}/Maya/modules/Redshift/{1}/Redshift2.5.4.0/Procedurals".format(
                         PROJECT_MAYA_PATH, MAYA_VERSION)],
                     REDSHIFT_LICENSEPATH=[REDSHIFT_CONF['REDSHIFT_LICENSEPATH']])

MAYA_LOCATION =  """
"D:/Program Files/Autodesk/Maya{0}/bin/maya.exe" -noAutoloadPlugins -command "loadPlugin \\"projectConfiguration.py\\";projectConf -ls all -lp \\"{1}\\";"
""".format(MAYA_VERSION, __file__.replace('\\', '/'))



# nuke --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
NUKE_VERSION = '10.5'

PROJECT_NUKE_PATH = os.path.join(os.path.dirname(basePath), "Nuke")
NUKE_BAT_PATH = {
    # http://help.thefoundry.co.uk/nuke/8.0/content/user_guide/configuring_nuke/nuke_environment_variables.html
    'NUKE_PATH': ["{0}/{1}".format(PROJECT_NUKE_PATH, NUKE_VERSION)]
    # 'OFX_PLUGIN_PATH': [PROJECT_NUKE_PATH],
    # 'PYTHONPATH': [PROJECT_NUKE_PATH]

}

NUKE_LOCATION = '"C:/Program Files/Nuke{0}v2/Nuke{0}.exe" --nukex "{1}" "{2}"'.format(NUKE_VERSION, '', FILENAME)


# photoshop --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
PHOTOSHOP_VERSION = 'CC 2015'

PHOTOSHOP_BAT_PATH = {}

PHOTOSHOP_LOCATION = """
"C:/Program Files/Adobe/Adobe Photoshop {}/Photoshop.exe"
""".format(PHOTOSHOP_VERSION)

# shotgun rv -+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
RV_VERSION = '7.2.0'

RV_BAT_PATH = {}

RV_LOCATION = """
"C:/Program Files/Shotgun/RV-{}/bin/rv.exe"
""".format(RV_VERSION)

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
SUBSTANCE_VERSION = ''

SUBSTANCE_BAT_PATH = {}

SUBSTANCE_LOCATION = """
"D:/Program Files/Allegorithmic/Substance Painter/Substance Painter.exe"
"""

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
SYNTHEYES_VERSION = ''

SYNTHEYES_BAT_PATH = {}

SYNTHEYES_LOCATION = """
"C:/Program Files/Andersson Technologies LLC/SynthEyes/SynthEyes64.exe"
"""

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
UE_VERSION = '4.16'

UE_BAT_PATH = {}

UE_LOCATION = """
"D:/Epic Games/UE_{0}/Engine/Binaries/Win64/UE4Editor.exe"
""".format(UE_VERSION)

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
ZBRUSH_VERSION = '4R8'

ZBRUSH_BAT_PATH = {}

ZBRUSH_LOCATION = """
"D:/program Files/Pixologic/ZBrush {}/ZBrush.exe"
""".format(ZBRUSH_VERSION)

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#

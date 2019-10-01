#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2019/8/13 11:21
# @Email    : spirit_az@foxmail.com
# @Name     : menu_1054_PN_SXD.py
__author__ = 'miaochenliang'

# import--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import getpass
import psutil
import maya.mel as mel
import maya.cmds as cmds
import maya.utils as mutils


# functions -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def close_parent_process():
    """
    close shell
    :return:
    """
    parent_process = psutil.Process().parent()
    if parent_process and parent_process.name() == 'cmd.exe':
        parent_process.kill()


# functions -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def initMenu():
    # - Load User hotkeys
    # try:
    #     cmds.hotkeySet(getpass.getuser(), e=True, cu=True)
    #
    # except RuntimeError:
    #     cmds.hotkeySet(getpass.getuser(), src='Maya_Default')
    #     cmds.hotkeySet(getpass.getuser(), e=True, cu=True)
    #
    # except:
    #     pass

    # - maya main window
    mayaWin = mel.eval("global string $gMainWindow;$temp= $gMainWindow;")

    # - main menu
    cmds.menu(l='1054_PN_SXD', to=True, p=mayaWin)

    # General +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='General', i='general.png', sm=True, to=True)
    cmds.menuItem(d=True)
    cmds.menuItem(l='Pipeline tools', c='from CGTmW.Pipeline_tools import openUI;reload(openUI);openUI.show("mantis", "1054_PN_SXD")')
    # cmds.menuItem(l='Publish Work', c='from CGTmW.publish_CGTm import openUI;reload(openUI);openUI.show()')
    cmds.menuItem(l='VHQ Player', i='window_icon.png',
                  c='from CGTmW.Pipeline_tools.MCLPlayer import showInMaya;showInMaya.show()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Scene Optimize', c='from GNR.optimize import openUI;openUI.show()')

    cmds.menuItem(l='velocity Mst', c='from GNR.velMst import openUI;openUI.show()')
    cmds.menuItem(l='Move_Trans', c='from GNR.scripts import move_trans;move_trans.main()')

    cmds.menuItem(d=True)
    cmds.menuItem(l='%s import double reference' % "(1)", c='from GNR.reference_edit import edit_ref_ns;'
                                                            'edit_ref_ns.im_double_ref()')
    cmds.menuItem(l='%s remove double namespace' % "(2)", c='from GNR.reference_edit import edit_ref_ns;'
                                                            'edit_ref_ns.rv_double_ns()')
    cmds.menuItem(l='del all namespace', c='from GNR.reference_edit import edit_ref_ns;'
                                           'edit_ref_ns.del_all_namespace()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Reload reference', c='from  GNR.reference_edit import openUI;openUI.show()')
    cmds.setParent('..', m=True)
    # Checking+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Checking+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Checking+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Checking', sm=True, to=True)
    # asset
    cmds.menuItem(l='Asset', sm=True)
    cmds.menuItem(l='model', c='from GNR.Check.asset.model import openUI;openUI.show()')
    cmds.menuItem(l='Shader', c='from GNR.Check.asset.Shader import openUI;openUI.show()')
    cmds.menuItem(l='Rig', c='from GNR.Check.asset.Rig import openUI;openUI.show()')
    cmds.menuItem(l='Fur', c='from GNR.Check.asset.Fur import openUI;openUI.show()')
    cmds.setParent('..', m=True)

    # shot
    cmds.menuItem(l='Shot', sm=True)
    cmds.menuItem(l='MatchMove', c='from GNR.Check.shot.MatchMove import openUI;openUI.show()')
    cmds.menuItem(l='layout', c='from GNR.Check.shot.lay import openUI;openUI.show()')
    cmds.menuItem(l='animation', c='from GNR.Check.shot.anim import openUI;openUI.show()')
    cmds.setParent('..', m=True)

    cmds.setParent('..', m=True)
    # Modeling+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Modeling+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Modeling+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Modeling', i='modeling.png', sm=True, to=True)
    cmds.menuItem(l='Start Work', i='cloud_download.png',
                  c="mel.eval('source \"scripts/CreateModelOutlineGroup.mel\";')")
    cmds.menuItem(l='meshReduceTool', c="from MOD.meshReduceTool import openUI;openUI.show()")
    cmds.menuItem(d=True)
    cmds.menuItem(l='SHAPESBrush', c='mel.eval("SHAPESBrush")')
    cmds.menuItem(l='AbSymMesh', c="mel.eval('source \"scripts/abSymMesh.mel\";abSymMesh;')")
    cmds.menuItem(l='UV Transfer', c='mel.eval("source \\"scripts/srbUVTransfer.mel\\";srbUVTransfer;")')
    cmds.menuItem(l='File Texture Manager',
                  c='mel.eval("source \\"scripts/FileTextureManager.mel\\";FileTextureManager;")')
    cmds.menuItem(l='djPFXUVs', c='from MOD.djPFXUVs import djPFXUVs;djPFXUVs.layoutUI()')
    cmds.menuItem(l='Wp Rename', c='mel.eval("source \\"scripts/wp_rename.mel\\";wp_rename;")')
    cmds.menuItem(l='NSUV Tool', c='import NSUV;NSUV.UI.createUI() ')
    cmds.menuItem(l='model edit Tool', c='from MOD.model_edit_tools import openUI;openUI.show() ')
    cmds.menuItem(l='UVDeluxe', c='from MOD.UVDeluxe import uvdeluxe;uvdeluxe.createUI()')
    cmds.menuItem(l='selectMeshByPolyCount',
                  c='from MOD.selectMeshByPolyCount import openUI;reload(openUI);openUI.show()')
    cmds.menuItem(l='proceduralBuilding', c='from MOD.proceduralBuilding import makeBuilding;makeBuilding.show()')
    # cmds.menuItem(l='reLoadUVLayout', c='from GNR.scripts import createShelf;createShelf.UVLayout()')
    cmds.setParent('..', m=True)
    # Surfacing--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Surfacing--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Surfacing--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Shading', i='surfacing.png', sm=True, to=True)
    cmds.menuItem(d=True)
    cmds.menuItem(l='replace fileTex',
                  c='from SUR.replace_fileTex import replace_fTex;replace_fTex.show()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='shader brown',
                  c='from SUR.shadE_brown import openUI;openUI.show()')

    cmds.menuItem(l='shader builder',
                  c='from SUR.shaderBuilder import openUI;openUI.show()')

    cmds.menuItem(l='texturePathSearchr',
                  c='from SUR.texturePathSearch import openUI;openUI.show()')

    cmds.menuItem(d=True)
    cmds.setParent('..', m=True)

    # Rigging +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Rigging +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Rigging +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Rigging', i='rigging.png', sm=True, to=True)
    cmds.menuItem(l='Start Work', i='cloud_download.png',
                  c='mel.eval("source \\"scripts/CreateRiggingOutlineGroup.mel\\";")')
    cmds.menuItem(d=True)
    cmds.menuItem(l='load AM_Tools', c='import amTools')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Weight Driver Edit RBF',
                  c='mel.eval("source \\"scripts/weightDriverEditRBF.mel\\";weightDriverEditRBF;")')
    cmds.menuItem(l='Copy Driven Key', c='from RIG.copyDKey import openUI;openUI.show()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='GuideBuilder (Rigger)', c='from RIG import Rigger;import GuideBuilder;GuideBuilder.main()')
    cmds.menuItem(l='Stepper (Rigger)', c='from RIG import Rigger;import Stepper;Stepper.main()')
    cmds.menuItem(l='weightMap (Rigger)', c='from RIG import Rigger;import weightMap;weightMap.main()')
    cmds.menuItem(l='Coder (Rigger)', c='from RIG import Rigger;import Coder;Coder.main()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='hyperRealMeshParent', c='mel.eval("source \\"scripts/hyperRealMeshParent.mel\\";'
                                             'hyperRealMeshParent;")')
    cmds.menuItem(l='morphTimeBlend', c='mel.eval("source \\"morphTimeBlend/rgMorphTimingBlendUI.mel\\";'
                                        'rgMorphTimingBlendUI();")')
    cmds.menuItem(l='geometryWalker', c='from RIG.geometryWalker.QT import pickWalker_UI;pickWalker_UI.pickWalkerUI()')
    cmds.menuItem(l='ngSkinTools', c='from ngSkinTools.ui.mainwindow import MainWindow;MainWindow.open()')
    cmds.menuItem(l='dslSculpt', c='from RIG.dslSculpt import dslSculptInbetweenEditor;'
                                   'dslSculptInbetweenEditor.SculptInbetweenEditor().ui()')
    cmds.menuItem(l='Skiin', c='from RIG.skiin import Skiin;Skiin.Skiin_UI()')
    cmds.setParent('..', m=True)

    # MatchMove--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # MatchMove--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # MatchMove--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='MatchMove', i='matchmove.png', sm=True, to=True)
    cmds.menuItem(l='Start Work', i='cloud_download.png',
                  c='from GNR.VSD import sd_hierarchy;sd_hierarchy.create_top_groups()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Survey Solver', c='mel.eval("source \\"scripts/SS_Converter.mel\\";")')
    cmds.menuItem(l='Get 3D Position', c='mel.eval("source \\"scripts/wh_get3DPosition\\";wh_get3DPosition;")')
    cmds.menuItem(l='Pan To Follow', c='from TRC import pan_to_follow;pan_to_follow.main()')
    cmds.menuItem(l='Synth Eyes', c='mel.eval("source \\"scripts/synthEyes.mel\\";")')
    cmds.menuItem(l='Back Face Culling', c='mel.eval("source \\"scripts/backFaceCulling.mel\\";")')
    cmds.menuItem(l='Precision', c='mel.eval("source \\"scripts/precision.mel\\";")')
    cmds.menuItem(l='Manip Cam Aligin', c='from TRC.scripts import manipCamAligin;manipCamAligin.manipCamAlign()')
    cmds.menuItem(l='Retime', c='from TRC.scripts import Retimer;Retimer.main()')
    cmds.menuItem(l='Filter Curve Tool', c='from TRC.scripts import filterCurveTool;filterCurveTool.fct_main()')
    cmds.menuItem(l='Export To AE', c='mel.eval("source \\"scripts/export2ae.mel\\";")')
    cmds.menuItem(l='Lock Length', c='mel.eval("source \\"scripts/lockLength.mel\\";")')
    cmds.menuItem(l='Create Cone', c='mel.eval("source \\"scripts/createCone.mel\\";")')
    cmds.menuItem(l='PlayBlast', c='mel.eval("source \\"scripts/playBlast.mel\\";")')
    cmds.menuItem(l='Render Marker Tool', c='from TRC.scripts import renderMarkerTool;renderMarkerTool.show()')
    cmds.menuItem(l='Render Wireframe Tool', c='from TRC.scripts import renderWireframeTool;renderWireframeTool.show()')
    cmds.menuItem(l='Create Nuke Project', c='from TRC.scripts import createNukeProject;'
                                             'createNukeProject.UI()')
    cmds.menuItem(l='Smooth Keys Tool', c='from TRC.smoothKey import openUI;openUI.show()')
    cmds.menuItem(l='Export and Refrence Assets', c='from TRC.scripts import convert_assets_to_ref;'
                                                    'convert_assets_to_ref.doIt()')
    cmds.menuItem(l='Create Loc By Point', c='from VFX.scripts import crtContainLoc;'
                                             'crtContainLoc')
    cmds.menuItem(l='checkRes', c='from TRC.scripts import checkRes;checkRes.main()')

    cmds.menuItem(l='TX StickyPoint', c='from TRC.tx_stickyController import ui as tx_StickyController_ui;tx_StickyController_ui.StickyControllerUI()')

    cmds.setParent('..', m=True)

    # Layout--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Layout--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Layout--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Layout', i='layout.png', sm=True, to=True)
    cmds.menuItem(d=True)
    cmds.menuItem(l='Reference Switcher', c='from LAY.ReferenceSwitcher import UI;UI.UI()')
    cmds.menuItem(l='Export and Refrence Assets', c='from LAY.scripts import convert_assets_to_ref;'
                                                    'convert_assets_to_ref.doIt()')
    cmds.menuItem(l='remove sel reference', c='from LAY.scripts import rm_sel_reference;'
                                              'rm_sel_reference.remove_ref()')
    cmds.menuItem(l='objectScatterTool', c='from LAY.Scattering import objectScatterTool;objectScatterTool.show()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='SwitchLOD050', c='mel.eval("source \\"scripts/ass.mel\\";")')
    cmds.menuItem(l='SwitchLOD250', c='mel.eval("source \\"scripts/assB.mel\\";")')
    cmds.setParent('..', m=True)
    # Animation--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Animation--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Animation--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Animation', i='animation.png', sm=True, to=True)
    cmds.menuItem(d=True)
    cmds.menuItem(l='Export ABC', c='from ANI.export_abc import openUI;openUI.show()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Anim Blast', c='from ANI.playblast import openUI;openUI.show()')
    cmds.menuItem(l='animation manager', c='from ANI.animationManager import tx_animationManager_ui;'
                                           'tx_animationManager_ui.show()')
    cmds.menuItem(l='animation manager new', c='from ANI.animationManager_new import tx_animationManager_ui;'
                                               'tx_animationManager_ui.newShow()')
    cmds.menuItem(l='create Motion Curve', c='from ANI.CreateCurves import openUI;'
                                             'openUI.show()')
    cmds.menuItem(l='Body Motion Capture Tool', c='from ANI.bodyMotionCapture import setMotion;'
                                                  'setMotion.setMotionUI()')
    cmds.menuItem(l='check Animation Color', c='from ANI.scripts import checkColor;'
                                               'checkColor.show()')
    cmds.menuItem(l='install MGTools', c='from ANI.scripts import install_MG;install_MG.install_MG()')
    cmds.menuItem(d=True)
    cmds.menuItem(l='Auto Switcher Shader', c='from ANI.vp20switcher import openUI;openUI.door();'
                                              'from CGTmW.publish_CGTm.module.Shot.Animation import assign_shader;'
                                              'assign_shader.assign_shader_all()')
    cmds.menuItem(l='vp20_Switcher_Lambert', c='from ANI.vp20switcher import openUI;openUI.door()')
    cmds.menuItem(l='vp20_Assign_Shader', c='from CGTmW.Pipeline_tools.module.shot.Animation import assign_shader;'
                                            'assign_shader.assign_shader_all()')

    cmds.menuItem(d=True)
    cmds.setParent('..', m=True)
    # Effects-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Effects-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Effects-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Effects', i='effacts.png', sm=True, to=True)
    cmds.menuItem(d=True)
    cmds.menuItem(l='replace texture path', c='from VFX.rp_yetiTex_path import openUI;'
                                              'openUI.show()')
    cmds.menuItem(l='Shatter', i='cloud_upload.png',
                  c='from VFX.IShatter import IShatterEXE;reload(IShatterEXE)')

    cmds.menuItem(l='nCloth Template', c='from VFX.NClothTemplate import openUI;'
                                         'openUI.show()')
    cmds.menuItem(l='Submit NCloth To Deadline ', c='from VFX.SubmitNClothToDeadline import openUI;'
                                                    'openUI.show()')
    cmds.menuItem(l='Submit Miarmy To Deadline ', c='from VFX.SubmitMiarmyToDeadline import openUI;'
                                                    'openUI.show()')
    cmds.menuItem(l='nHairRebuild', c='from VFX.nHairRebuild import openUI;openUI.show()')
    cmds.menuItem(l='create Motion Curve', c='from ANI.CreateCurves import openUI;'
                                             'openUI.show()')
    cmds.menuItem(l='Create Loc By Point', c='from TRC.scripts import createLocByPoint;'
                                             'createLocByPoint.run()')
    cmds.setParent('..', m=True)

    # CFX  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='CFX', sm=True, to=True)
    cmds.menuItem(l='assign Yeti in asset',
                  c="from CGTmW.publish_CGTm.module.Asset.Fur import yeti_in;yeti_in.main(k=1)")
    cmds.menuItem(l='assign Yeti in shot ',
                  c="from CGTmW.publish_CGTm.module.Asset.Fur import yeti_in;yeti_in.main(k=0)")
    cmds.menuItem(l='assign Yeti in Lgt ',
                  c="from CGTmW.publish_CGTm.module.Asset.Fur import yeti_in;yeti_in.main(k=0, Lgt=1)")
    cmds.setParent('..', m=True)

    # Lighting+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Lighting+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # Lighting+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Lighting', i='lighting.png', sm=True, to=True)
    cmds.menuItem(l='Publish Work', i='cloud_upload.png', c='from LGT.lgt_Publish import openUI;openUI.show()')
    cmds.menuItem(l='meshReduceTool', c="from MOD.meshReduceTool import openUI;openUI.show()")

    cmds.menuItem(d=True)
    cmds.menuItem(l='Submit to Deadline', c='from LGT.MayaToDeadline import dl_maya_open_ui;reload(dl_maya_open_ui);dl_maya_open_ui.deadline_show()')
    cmds.menuItem(d=True)

    cmds.menuItem(l='Light Group', c='mel.eval("source \\"scripts/LightGroup.mel\\";LightGroup();")')
    cmds.menuItem(l='Identify Yeti', c='from LGT.yeti_IO import openUI;openUI.show()')
    cmds.menuItem(l='Lighting Output', c='from LGT.lgtOutput import readLight;readLight.run()')
    cmds.menuItem(l='LGT Edit Tools', c='from LGT.lgt_edit_tools import openUI;openUI.show()')
    cmds.menuItem(l='Light Tools', c='from LGT.LightingTool import openUI;openUI.show()')
    cmds.menuItem(l='Render Layer Tools ', c='from LGT.lightToolsly import openUI;openUI.show()')
    # cmds.menuItem(l='LGTRig Tools', c='from LGT.LGTRig_Tools import openUI;openUI.show()')
    cmds.menuItem(l='nHairRebuild', c='from VFX.nHairRebuild import openUI;openUI.show()')

    cmds.setParent('..', m=True)

    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Redshift', sm=True, to=True)
    cmds.menuItem(l='MaterialManager', c='from REDS.DW_MaterialManager import userLauncher;reload(userLauncher)')

    cmds.setParent('..', m=True)

    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(l='Environment', sm=True, to=True)
    cmds.menuItem(l='Publish Work',
                  c="from ENV.env_publish import env_open_ui;reload(env_open_ui);env_open_ui.show_win()")
    cmds.menuItem(l='CGTm To Deadline',
                  c='from CGTmW.cgtw_to_deadline2 import dl_open_ui;reload(dl_open_ui);dl_open_ui.deadline_ui_show()')
    cmds.menuItem(l='Publish Work New',
                  c="from ENV.maya_env_cgtw_publish import maya_env_cgtw_publish_open_ui;reload(maya_env_cgtw_publish_open_ui);maya_env_cgtw_publish_open_ui.show()")

    cmds.setParent('..', m=True)
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    cmds.menuItem(d=True)
    cmds.menuItem(l='Help', i='github.png')
    cmds.setParent('..', m=True)
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #
    # --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-- #


def run():
    # pass
    close_parent_process()
    mutils.executeDeferred(initMenu)

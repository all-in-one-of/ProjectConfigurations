#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      : 2019/8/20 16:51
# Email     : spirit_az@foxmail.com
# File      : shelf_1054_PN_SXD.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
shelves_pipelineTools = {'name': 'pipeline', 'label': '1054_PN_SXD',
                         'tools': [('pipelineTools', 'pipelineTools', 'from pipelineTools.scripts import openUI\n'
                                                                      'reload(openUI)\n'
                                                                      'openUI.show("cgtw", "1054_PN_SXD")', 1,
                                    'PLASMA_App')
                                   ]

                         }

SHELVES_TABLES = [shelves_pipelineTools]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  23 11:33:58 2019

@author: 1191: ritesh
"""
# global changable configuration
CONFIG = {
    # we can select our own backup limit
    'backup_limit': 5,
    # specify backup folder location, we can provide relative as well as absolute path, for absolute path put '/' before path
    'backup_folder_loc': '/mnt/backups/client/web_desktop/',
    # 'backup_folder_loc': 'Backup/',
    # specify the UI repository path
    # 'ui_codebase_path': '/home/platform/codebase/node/UI/Demo-app',
    'ui_codebase_path': '/mnt/codebase/client/web_desktop/UI/Demo-app',
    # deployed_folder_loc relative to ui_codebase_path
    'deployed_folder_loc': '/mnt/deployed/client/web_desktop',
    # specify ng build configuration (dev,qa,preprod,prod)
    'configuration_type': 'dev',
    # specify your branch name (master,qa,preprod,prod)
    'active_branch': 'master'
}
WEBCONFIG = {
    # we can select our own backup limit
    'backup_limit': 5,
    # specify backup folder location, we can provide relative as well as absolute path, for absolute path put '/' before path
    'backup_folder_loc': '/mnt/backups/client/web_mobile/',
    # 'backup_folder_loc': 'Backup/',
    # specify the UI repository path
    # 'ui_codebase_path': '/home/platform/codebase/node/UI/Demo-app',
    'ui_codebase_path': '/mnt/codebase/client/web_mobilep/4TIGOANDROID',
    # deployed_folder_loc relative to ui_codebase_path
    'deployed_folder_loc': '/mnt/deployed/client/web_mobile',
    # specify ng build configuration (qa,prod,4tigowebmobile/dev)
    'configuration_type': '4tigowebmobile/dev',
    # specify your branch name
    'active_branch': '4tigowebmobile/dev'
}

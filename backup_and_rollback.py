#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  27 11:33:58 2019

@author: 1191: ritesh
"""
# create backup folder name based on current date and count

from deployUIConfig import CONFIG
from deployUIConfig import WEBCONFIG

import subprocess as sp
from datetime import date
import os
from setup import I_CONFIG as path

# import json
today = date.today().strftime("%d-%m-%Y")
# global configuration from CONFIG file
backup_limit = CONFIG['backup_limit']
backup_folder_loc = CONFIG['backup_folder_loc']
ui_codebase_path = CONFIG['ui_codebase_path']
# deployed_folder_loc relative to ui_codebase_path
deployed_folder_loc = CONFIG['deployed_folder_loc']
# default deployment folder location
default_deployed_loc = ui_codebase_path+'/dist/Demo-app'

# gets config from config files
def change_config():
    # global configuration from CONFIG file
    global backup_limit 
    backup_limit = WEBCONFIG['backup_limit']
    global backup_folder_loc 
    backup_folder_loc = WEBCONFIG['backup_folder_loc']
    global ui_codebase_path 
    ui_codebase_path = WEBCONFIG['ui_codebase_path']
    # deployed_folder_loc relative to ui_codebase_path
    global deployed_folder_loc 
    deployed_folder_loc = WEBCONFIG['deployed_folder_loc']
    global default_deployed_loc
    default_deployed_loc = ui_codebase_path+'/build'

def create_backup_folder_name(count, with_date=True):
    if with_date:
        # used in case of creating backup folder
        return str(backup_folder_loc+"Backup_"+str(count)+"_"+str(today))
    else:
        # used in case of finding and renaming backup folder
        return str(backup_folder_loc+"Backup_"+str(count)+"_*")

# handles backup folder whenever backup folders exceeds the limit


def handle_overflow_backup(count):
    # remove the backup number 1 as it is the oldest
    sp.call(path['rm']+" -rf "+create_backup_folder_name(1, False), shell=True)
    # rename all the folder such as 2 -> 1, 3 -> 2 and so on
    for i in range(2, backup_limit+1):
        # present folder name
        folder_name = sp.check_output(
            path['find']+" "+backup_folder_loc+"* -type d -name 'Backup_"+str(i)+"*'", shell=True, universal_newlines=True)
        splitted_name = folder_name.strip().split('/')
        folder_name = str(splitted_name[-1])
        # new folder name
        new_folder_name = folder_name[:7]+str(i-1)+folder_name[8:]
        sp.call([path["mv"], backup_folder_loc+folder_name, backup_folder_loc+new_folder_name])
    # call method to create backup folder
    create_backup()

# create backup folder


def create_backup(mode = 'ui'):
    if mode == 'web' :
        change_config()
    print('\033[1;32;40m Creating Backup... ')
    # print(sp.Popen(['pwd']))

    total_backup_count = sp.Popen(
        [path['ls'], backup_folder_loc, '-1'], stdout=sp.PIPE)
    total_backup_count = sp.check_output(
        [path['wc'], '-l'], stdin=total_backup_count.stdout, universal_newlines=True)
    total_backup_count = int(total_backup_count.strip())
    # print(total_backup_count)
    if total_backup_count < backup_limit:
        # os.makedirs(create_backup_folder_name(total_backup_count+1))
        sp.call([path["mkdir"], "-p", create_backup_folder_name(total_backup_count+1)])
        # copy new build to backup folder
        sp.call([path["cp"], "-r", default_deployed_loc,
                    create_backup_folder_name(total_backup_count+1)])
    
    else:
        handle_overflow_backup(total_backup_count)

# rollback feature


def rollback(mode = 'ui'):
    if mode == 'web' :
        change_config()
    total_backup_count = sp.Popen(
        [path['ls'], backup_folder_loc, '-1'], stdout=sp.PIPE)
    total_backup_count = sp.check_output(
        [path['wc'], '-l'], stdin=total_backup_count.stdout, universal_newlines=True)
    total_backup_count = int(total_backup_count.strip())
    if total_backup_count > 1:
        # os.removedirs(deployed_folder_loc+"Demo-app")
        serverStatus = sp.call(path['rm']+' -rf '+deployed_folder_loc+"/build &&"+path['cp']+" -r " +
                               create_backup_folder_name(total_backup_count-1)+" "+deployed_folder_loc, shell=True)
        if serverStatus == 0:
            print('\033[1;32;40m rollback successed......')
            sp.call(
                path['rm']+" -rf "+create_backup_folder_name(total_backup_count, False), shell=True)
    else:
        print('\033[1;31;40m No previous backup found: \n')

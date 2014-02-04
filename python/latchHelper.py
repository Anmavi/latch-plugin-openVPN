'''
 This script helps to integrate latch into system
 Copyright (C) 2013 Eleven Paths

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation; either
 version 2.1 of the License, or (at your option) any later version.
 
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.
 
 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
'''

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# vim: set fileencoding=utf-8
# Run as root

import sys
import os
import urllib.request
import latch


LATCH_PATH = "/etc/openvpn/latch/"

LATCH_ACCOUNTS = "/etc/openvpn/latch/latch_accounts"
LATCH_CONFIG =  "/etc/openvpn-latch.conf"
LATCH_HOST = "https://latch.elevenpaths.com"

LATCH_OPENVPN_SUDOERS = "/etc/sudoers.d/latch_openvpn_conf"
LATCH_LOGIN_PAM_CONFIG = "/etc/pam.d/latch-login"
LATCH_PAM_SO = "/lib/security/pam_latch.so"

LOGIN_PAM_CONFIG = "/etc/pam.d/login"

LATCH_PLUGIN_GUI = LATCH_PATH + "latchPluginGUI.py"
SETTINGS_PLUGIN_GUI = LATCH_PATH + "settingsGUI.py"
PAIR_PLUGIN = LATCH_PATH + "pair.py"
UNPAIR_PLUGIN = LATCH_PATH + "unpair.py"
SETTINGS_PLUGIN = LATCH_PATH + "settings.py"
LATCH_HELPER_PLUGIN = LATCH_PATH + "latchHelper.py"

LATCH_API = LATCH_PATH + "latch.py"



def getConfigParameter(name):

    # read latch config file
    f = open(LATCH_CONFIG,"r");
    lines = f.readlines();
    f.close();

    # find parameter
    for line in lines:
        if line.find(name) != -1:
            break;

    words = line.split();   
    if len(words) == 3:
        return words[2];
    return None;

def getAccountId(user):

    if os.path.isfile(LATCH_ACCOUNTS):
        # read latch_accounts file
        f = open(LATCH_ACCOUNTS,"r");
        lines = f.readlines();
        f.close();

        for line in lines:
            if line.find(user) != -1:
                words = line.split();
                if len(words) == 2:
                    return words[1];
                break; 
        return None;
    '''
    else:
        print("Error: latch_accounts file doesn't exist")
        exit()
    '''

def isPair(user):
    if os.path.isfile(LATCH_ACCOUNTS):
        # read latch_accounts file
        f = open(LATCH_ACCOUNTS,"r")
        lines = f.readlines()
        f.close()
        # find user
        found = False          
        for line in lines:
            if line.find(user) != -1:
                found = True
                break
        if found:
            return True
        return False
    '''
    else:
        print("Error: latch_accounts file doesn't exist")
        exit()
    '''

def deleteAccount(accountId):
    # read latch_accounts file
    f = open(LATCH_ACCOUNTS,"r")
    lines = f.readlines()
    f.close()
    # delete latch account
    f = open(LATCH_ACCOUNTS,"w")
    for line in lines:
        if line.find(accountId) == -1 :
            f.write(line);
    f.close();

def addAccount(user, accountId):
    if os.path.isfile(LATCH_ACCOUNTS):
        # add latch account
        f = open (LATCH_ACCOUNTS, "a")
        f.write(user + ": " + accountId)
        f.close();
    else:
        # add latch account  
        fd = os.open (LATCH_ACCOUNTS, os.O_WRONLY | os.O_CREAT, int("0600",8))
        f = os.fdopen(fd)
        f.write(user + ": " + accountId + "\n");
        f.close();    
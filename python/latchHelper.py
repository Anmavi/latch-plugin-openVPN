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


import sys
import os
import latch


PLUGIN_NAME = "OpenVPN - latch"

LATCH_PATH = "/usr/lib/latch/"
LATCH_OPENVPN_PATH = LATCH_PATH + "openvpn/"

LATCH_ACCOUNTS = LATCH_OPENVPN_PATH + ".latch_accounts"
LATCH_CONFIG =  "/etc/openvpn-latch.conf"
LATCH_HOST = "https://latch.elevenpaths.com"

LOGIN_PAM_CONFIG_FILE = "/etc/pam.d/login"
OPENVPN_PAM_CONFIG_FILE = "/etc/pam.d/openvpn"

LATCH_PAM_SO = "/lib/security/pam_latch.so"

LATCH_PAM_CONFIG = "auth        required        " + LATCH_PAM_SO + "    accounts=" + LATCH_ACCOUNTS + "    config=" + LATCH_CONFIG

PAIR_BIN = "/usr/bin/pairOVPN"
UNPAIR_BIN = "/usr/bin/unpairOVPN"
PLUGIN_BIN = "/usr/bin/latchOVPN"
SETTINGS_BIN = "/usr/sbin/config_latchOVPN"

LATCH_PLUGIN_GUI = LATCH_OPENVPN_PATH + "latchPluginGUI.py"
SETTINGS_PLUGIN_GUI = LATCH_OPENVPN_PATH + "settingsGUI.py"
PAIR_PLUGIN = LATCH_OPENVPN_PATH + "pair.py"
UNPAIR_PLUGIN = LATCH_OPENVPN_PATH + "unpair.py"
SETTINGS_PLUGIN = LATCH_OPENVPN_PATH + "settings.py"
LATCH_HELPER_PLUGIN = LATCH_OPENVPN_PATH + "latchHelper.py"

LATCH_API = LATCH_OPENVPN_PATH + "latch.py"


def getConfigParameter(name, configFile=LATCH_CONFIG):

    # read latch config file
    try:
        f = open(configFile,"r")
    except IOError as e:
        return None

    lines = f.readlines()
    f.close()

    # find parameter
    for line in lines:
        if line.find(name) != -1:
            break;

    words = line.split()
    if len(words) == 3:
        return words[2]
    return None

def replaceConfigParameters(newAppId, newSecret):

    # write config file
    fd = os.open (LATCH_CONFIG, os.O_WRONLY | os.O_CREAT, int("0600",8))
    f = os.fdopen(fd,"w")
    f.write("#\n")
    f.write("# Configuration file for " + PLUGIN_NAME + "\n")
    f.write("#\n")
    f.write("\n")
    f.write("# Identify your Application\n")
    f.write("# Secret key value\n")
    f.write("#\n")
    f.write("app_id = " + newAppId + "\n")
    f.write("\n")
    f.write("# Application ID value\n")
    f.write("#\n")
    f.write("secret_key = " + newSecret + "\n")
    f.close()

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
        f.write(user + ": " + accountId + "\n")
        f.close();
    else:
        # add latch account  
        fd = os.open (LATCH_ACCOUNTS, os.O_WRONLY | os.O_CREAT, int("0600",8))
        f = os.fdopen(fd)
        f.write(user + ": " + accountId + "\n");
        f.close();  

  

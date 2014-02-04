#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# vim: set fileencoding=utf-8
# Run as root

'''
 This script allows to install latch plugin in openvpn Server in some UNIX systems (like Linux)
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
import shutil

from latchHelper import *


if len(sys.argv) == 3 and sys.argv[1] == "-f":
    # read config file
    try:
        f = open(sys.argv[2],"r")
    except IOError as e:
        print ('cannot open', sys.argv[2])
        exit()

    lines = f.readlines()
    f.close()
    # write config file
    f = open(LATCH_CONFIG,"w")
    f.writelines(lines)
    f.close()
else:
    print("use 'install.py -f <file.conf>'");
    exit();

if not os.path.isfile(LATCH_LOGIN_PAM_CONFIG): 
    # add latch-login PAM configuration
    fd = os.open (LATCH_LOGIN_PAM_CONFIG, os.O_CREAT, int("0440",8)) 
    f = open(LATCH_LOGIN_PAM_CONFIG,"a")

    # read login PAM config file
    f = open(LOGIN_PAM_CONFIG,"r")
    lines = f.readlines()
    f.close()

    # write latch-login PAM config file
    f = open(LATCH_LOGIN_PAM_CONFIG,"a")
    f.writelines(lines)
    f.write("auth       required	    " + LATCH_PAM_SO + "    accounts=" + LATCH_ACCOUNTS + "    config=" + LATCH_CONFIG)
    f.close()

    # install latch in /etc/openvpn
    os.mkdir(LATCH_PATH)

    os.open (LATCH_PLUGIN_GUI, os.O_CREAT, int("0100",8))
    shutil.copyfile('latchPluginGUI.py', LATCH_PLUGIN_GUI)

    os.open (SETTINGS_PLUGIN_GUI, os.O_CREAT, int("0100",8))
    shutil.copyfile('settingsGUI.py', SETTINGS_PLUGIN_GUI)

    os.open (PAIR_PLUGIN, os.O_CREAT, int("0100",8))
    shutil.copyfile('pair.py', PAIR_PLUGIN)

    os.open (UNPAIR_PLUGIN, os.O_CREAT, int("0100",8))
    shutil.copyfile('unpair.py', UNPAIR_PLUGIN)

    os.open (SETTINGS_PLUGIN, os.O_CREAT, int("0100",8))
    shutil.copyfile('settings.py', SETTINGS_PLUGIN)

    os.open (LATCH_HELPER_PLUGIN, os.O_CREAT, int("0100",8))
    shutil.copyfile('latchHelper.py', LATCH_HELPER_PLUGIN)

    os.open (LATCH_API, os.O_CREAT, int("0100",8))
    shutil.copyfile('latch.py', LATCH_API)


    # add latch_accounts file 
    fd = os.open (LATCH_ACCOUNTS, os.O_CREAT, int("0600",8)) 

    # add sudo privileges for latch execution
    fd = os.open (LATCH_OPENVPN_SUDOERS, os.O_CREAT, int("0440",8))
    f = open(LATCH_OPENVPN_SUDOERS,"a")
    f.write("ALL ALL= NOPASSWD: " + LATCH_PLUGIN_GUI + "\n");
    f.write("ALL ALL= NOPASSWD: " + PAIR_PLUGIN + "\n");
    f.write("ALL ALL= NOPASSWD: " + UNPAIR_PLUGIN + "\n");
    f.close();

    print("Installed")
else:
    print("latch-auth-pam openvpn plugin is already installed")

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# vim: set fileencoding=utf-8
# Run as root

'''
 This script allows to uninstall latch plugin from openvpn Server in some UNIX systems (like Linux)
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



import os
import shutil

from latchHelper import *


if os.path.isfile(OPENVPN_PAM_CONFIG_FILE):
    # read PAM config file
    f = open(OPENVPN_PAM_CONFIG_FILE,"r");
    lines = f.readlines();
    f.close();
    # delete latch PAM 
    f = open(OPENVPN_PAM_CONFIG_FILE,"w");
    for line in lines:
        if line.find(LATCH_PAM_CONFIG) == -1 :
            f.write(line);
    f.close();

if os.path.isfile(LATCH_ACCOUNTS):
    os.remove(LATCH_ACCOUNTS)
if os.path.isfile(LATCH_CONFIG):
    os.remove(LATCH_CONFIG)
if os.path.isdir(LATCH_PATH):
    shutil.rmtree(LATCH_PATH)
if os.path.isfile("/usr/bin/pairOpenVPN"):
    os.remove("/usr/bin/pairOpenVPN")
if os.path.isfile("/usr/bin/unpairOpenVPN"):
    os.remove("/usr/bin/unpairOpenVPN")
if os.path.isfile("/usr/bin/latchOpenVPN"):
    os.remove("/usr/bin/latchOpenVPN")

print("Uninstall completed")

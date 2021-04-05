import xbmc
import xbmcgui

import sys
import os
import shutil

dry_run = True

def uninstall_server(): 
    '''Function to uninstall nfs server.'''
    if dry_run:
        line1 = "Uninstalling nfs-kernel-server"
        xbmcgui.Dialog().ok('kodi',line1)
    else:
        line1 = "Uninstalling nfs-kernel-server"
        xbmcgui.Dialog().ok('kodi',line1)
        source = "/etc/exports.bak"
        dest = "/etc/exports"
        os.system('sudo apt-get remove -y nfs-kernel-server')
        os.system("sudo rm /etc/exports")
        shutil.os.system('sudo cp "{}" "{}"'.format(source,dest))
        os.system("sudo rm /etc/exports.bak")
        os.system('/bin/bash -c "sudo systemctl restart nfs-kernel-server"')
        line1 = "Uninstall Complete"
        xbmcgui.Dialog().ok('kodi',line1)

dialog = xbmcgui.Dialog()
if not dialog.yesno('Kodi', 'Do you want to uninstall the NFS server?'):
    line1 = "Exiting Uninstall"
    xbmcgui.Dialog().ok('kodi',line1)
    sys.exit()

uninstall_server()

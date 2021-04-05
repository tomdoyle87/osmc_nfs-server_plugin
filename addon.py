"""
    Plugin to configure NFS Server on OSMC
"""

# -*- coding: UTF-8 -*-
# main imports
import xbmc
import xbmcgui
import xbmcaddon
import Kodi-nfs-server-setup
import Kodi-uninstall-nfs-server

# plugin constants
__plugin__ = "configure NFS Server on OSMC "
__author__ = "tomdoyle87"
__url__ = "https://osmc.tv/"
__git_url__ = "https://github.com/tomdoyle87/osmc_nfs-server_plugin"
__credits__ = "tomdoyle87"
__version__ = "0.0.1"

def select(heading, options, default=lambda: select_main):
    labels = [option['label'] for option in options]
    result = xbmcgui.Dialog().select(heading, labels)
    selected = options[result]
    if result == -1:
        log_debug("using default action")
        default()
        return
    selected['func'](selected)
    selected['complete']()

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_NFS_Sever')

def select_main():
    menu = [
            {'label': 'Install NFS Server', 'func': Popen('python Kodi-nfs-server-setup.py'), 'complete': select_main},
            {'label': 'Unstall NFS Server', 'func': Popen('Kodi-uninstall-nfs-server.py'), 'complete': select_main}
    ]
    select('NFS Server', menu, default=select_noop)

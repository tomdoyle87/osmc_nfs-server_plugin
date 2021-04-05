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

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_NFS_Sever')

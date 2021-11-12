"""
    Plugin to configure NFS Server on OSMC
"""

# -*- coding: UTF-8 -*-
# main imports
import xbmc
import xbmcgui
import xbmcaddon



# plugin constants
__plugin__ = "configure NFS Server on OSMC "
__author__ = "tomdoyle87"
__url__ = "https://osmc.tv/"
__git_url__ = "https://github.com/tomdoyle87/osmc_nfs-server_plugin"
__credits__ = "tomdoyle87"
__version__ = "0.0.1"


dialog = xbmcgui.Dialog()
if dialog.yesno('Kodi', 'Please select an option', yeslabel='Install NFS Server', nolabel='Uninstall NFS Server'):
    xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.OSMC_NFS_Sever/resources/lib/Kodi-nfs-server-setup.py)')
else:
    xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.OSMC_NFS_Sever/resources/lib/Kodi-uninstall-nfs-server.py)')

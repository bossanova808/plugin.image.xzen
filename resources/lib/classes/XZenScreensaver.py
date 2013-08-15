#imports
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon

from b808common import *

class XZenScreensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            log("ExitMonitor: sending exit_callback")
            self.exit_callback()

    def onInit(self):
        log("Screensaver: onInit")
        self.monitor = self.ExitMonitor(self.exit)
        self.root_type=ADDON.getSetting('ss_root_type')
        self.root_data=ADDON.getSetting('ss_root_data')
        log("Root type is: "+ str(self.root_type) +", root data is: " + self.root_data)

    def exit(self):
        log("Screensaver: Exit requested")
        self.close()

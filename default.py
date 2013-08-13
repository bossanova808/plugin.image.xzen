# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING. If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *

#imports
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import os

# Minimal code to import bossanova808 common code
ADDON           = xbmcaddon.Addon()
CWD             = ADDON.getAddonInfo('path')
RESOURCES_PATH  = xbmc.translatePath( os.path.join( CWD, 'resources' ))
LIB_PATH        = xbmc.translatePath(os.path.join( RESOURCES_PATH, "lib" ))

sys.path.append( LIB_PATH )

from b808common import *
from XZenScreensaver import *
from XZenPlugin import *

################################################################################
################################################################################
# MAIN
################################################################################
################################################################################

if __name__ == '__main__':

    #kick this off
    footprints()
 
    #there will be parameters if we're running as a plugin..
    if sys.argv[0]=='':
        SCREENSAVER=True
    else:    
        SCREENSAVER=False

    # Calles as a screensaver?  This will be blank
    if SCREENSAVER:
        log( "Running as screensaver" )
        screensaver_gui = XZenScreensaver('XZenScreensaver.xml' , CWD, 'Default')
        screensaver_gui.doModal()
        #when we drop back here we're out of the screensaver...
        log ("Xzen Screensaver Exited")
        del screensaver_gui
    # we're running as an image plugin...
    else:
        log( "Running as a Pictures addon" )
        plug = XZenPlugin()
 

    #and power this puppy down....
    footprints(startup=False)





from b808common import *
from XZenConstants import *
from XZenBridge import *

class XZenPlugin():

    #init basically does everything in this class...
    def __init__(self):

        #set up connection to ZenFolio
        self.zen = XZenBridge()
 
        #zero out core data between passes
        self.mode = None
        self.url = None
        self.galleryid=None
        self.group=None
        self.category=None
        self.categoryid=None
        self.choice=None
 
        #parse the parameters
        params=getParams()
       
        #try and get data from the paramters
        try:
            self.url=urllib.unquote_plus(params["url"])
        except:
            pass
        try:
            self.galleryid=int(params["galleryid"])
        except:
            pass
        try:
            self.mode=params["mode"]
        except:
            pass
        try:
            self.group=int(params["group"])
        except:
            pass
        try:
            self.category=params["category"]
        except:
            pass
        try:
            self.categoryid=params["categoryid"]
        except:
            pass
        try:
            self.choice=params["choice"]
        except:
            pass
        #if we're paging groups of photos, what is the starting offset?
        self.offset=0
        try:
            self.offset=int(params["offset"])
        except:
            pass

        log("Parameters parsed: " + str(params))

        #do something...
        self.action_mode()

        ################################################################################
        # FINISH OFF - set display mode appropriately, tell XBMC we're done, exit.

        #if we've just built a list of albums, force thumbnail mode
        if self.mode in galleryModes:
          log("Playable Items -> Trying to set thumnbnail mode...")
          xbmc.executebuiltin('Container.SetViewMode(500)')
        else:
          log("List Items -> Trying to set list mode...")
          xbmc.executebuiltin('Container.SetViewMode(50)')

        #and tell XBMC we're done adding items...
        xbmcplugin.endOfDirectory(THIS_PLUGIN)


    # Call the write function depending on the node balue   
    def action_mode(self):
        
        try:
            if self.mode==None or self.mode==MENU_ROOT:
                log( "Display XZen Root Menu" )
                self.zen.BuildMenuRoot()

            elif self.mode==MENU_USERGALLERIES:
                log( "Display XZen User Gallery" )
                self.zen.BuildUserGallery(self.group)

            elif self.mode==POPPHOTOS:
                log( "Display XZen Popular Photos")
                self.zen.ShowPopularPhotos(self.offset)

            elif self.mode==POPGALLERIES:
                log( "Display XZen Popular Galleries")
                self.zen.BuildMenuPopSets("Gallery",self.offset)

            elif self.mode==POPCOLLECTIONS:
                log( "Display XZen Popular Collections")
                self.zen.BuildMenuPopSets("Collection", self.offset)

            elif self.mode==RECENTPHOTOS:
                log( "Display XZen Recent Photos")
                self.zen.ShowRecentPhotos(self.offset)

            elif self.mode==RECENTGALLERIES:
                log( "Display XZen Recent Galleries")
                self.zen.BuildMenuRecentSets("Gallery",self.offset)

            elif self.mode==RECENTCOLLECTIONS:
                log( "Display XZen Recent Collections")
                self.zen.BuildMenuRecentSets("Collection", self.offset)

            elif self.mode==CATEGORIES:
                log( "Display XZen Categories")
                self.zen.BuildMenuCategories(self.category)

            elif self.mode==CATEGORY_OPTIONS:
                log( "Display XZen Category Options (Photos/Galleries/Collections)")
                self.zen.BuildMenuCategoryOptions(self.categoryid)

            elif self.mode==DISPLAY_CATEGORY:
                log( "Display XZen Category id: " + str (self.categoryid) )
                self.zen.AddCategory(self.categoryid,self.choice,self.offset)

            elif self.mode==DISPLAY_GALLERY:
                log( "Display XZen Gallery id: " + str (self.galleryid) )
                self.zen.AddGallery(self.galleryid)

            else:
                notify(LANGUAGE(30017))
                sys.exit()
        except:
            print_exc()


 
import gtk
import os

import sucker

class DownloadsTab(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self, False, 0)

        self._setup_menubar()

    def get_menubar_actiongroup(self):
        entries = (
            ('Downloads'  , None         , '_Downloads'          , None    , None ,None),
            ('NewDownload', gtk.STOCK_ADD, '_Create New Download', '<ctl>n', None , self._new_download_action),
        )

        action = gtk.ActionGroup('DownloadsTabAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'downloads-menubar.ui')
        with open(ui_file) as f:
            string = f.read()

        return action, string

    def _setup_menubar(self):
        entries = (
            ('Add', gtk.STOCK_ADD, None, None, None, self._new_download_action),
        )

        action = gtk.ActionGroup('DownloadTabAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'downloads-toolbar.ui')

        self._toolbar = gtk.UIManager()
        self._toolbar.add_ui_from_file(ui_file)
        self._toolbar.insert_action_group(action)

        self.pack_start(self._toolbar.get_widget('/ToolBar'), False, True, 0)
        #self.add_accel_group(self._menubar.get_accel_group())

    def _new_download_action(self, action):
        print ('New Download!!!')

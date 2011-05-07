import gtk
import os

import sucker

class DownloadsTab(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self, False, 0)

        self._setup_menubar()

    def _setup_menubar(self):
        entries = (
            ('Add', gtk.STOCK_ADD, None, None, None, None),
        )

        action = gtk.ActionGroup('DownloadTabAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'downloads-toolbar.ui')

        self._toolbar = gtk.UIManager()
        self._toolbar.add_ui_from_file(ui_file)
        self._toolbar.insert_action_group(action)

        self.pack_start(self._toolbar.get_widget('/ToolBar'), False, True, 0)
        #self.add_accel_group(self._menubar.get_accel_group())

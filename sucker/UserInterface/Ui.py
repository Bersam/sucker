import gtk
import os.path

import sucker
from PluginsDialog import PluginsDialog

class Ui(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.set_title('Sucker')
        self.resize(400, 400)

        self._box = gtk.VBox()
        self.add(self._box)

        self._setup_menubar()

    def set_plugin_infos(self, infos):
        self.plugin_infos = infos

    def _setup_menubar(self):
        entries = (
            ('File'   , None           , '_File'   , None     , None, None),
            ('Close'  , gtk.STOCK_CLOSE, None      , '<ctl>w' , None, self._close_action),
            ('Quit'   , gtk.STOCK_QUIT , None      , '<ctl>q' , None, self._quit_action),
            ('Edit'   , None           , '_Edit'   , None     , None, None),
            ('Plugins', None           , '_Plugins', None     , None, self._plugin_action),
        )

        action = gtk.ActionGroup('MenuBarAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'menubar.ui')

        self._menubar= gtk.UIManager()
        self._menubar.add_ui_from_file(ui_file)
        self._menubar.insert_action_group(action)

        self._box.pack_start(self._menubar.get_widget('/MenuBar'), False, True, 0)
        self.add_accel_group(self._menubar.get_accel_group())

    def _quit_action(self, action):
        self.emit('destroy')

    def _close_action(self, action):
        self.emit('destroy')

    def _plugin_action(self, action):
        dialog = PluginsDialog()
        dialog.create_rows(self.plugin_infos)
        dialog.run()
        dialog.destroy()

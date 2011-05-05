import os.path
from gi.repository import Gtk

import sucker

class Ui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_title('Sucker')
        self.resize(400, 400)

        self._box = Gtk.VBox()
        self.add(self._box)

        self._setup_menubar()

    def _setup_menubar(self):
        entries = (
            ('File' , None           , '_File', None     , None, None),
            ('Close', Gtk.STOCK_CLOSE, None   , '<ctl>w' , None, self._close_action),
            ('Quit' , Gtk.STOCK_QUIT , None   , '<ctl>q' , None, self._quit_action),
        )

        action = Gtk.ActionGroup('MenuBarAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'menubar.ui')

        self._menubar= Gtk.UIManager()
        self._menubar.add_ui_from_file(ui_file)
        self._menubar.insert_action_group(action)

        self._box.pack_start(self._menubar.get_widget('/MenuBar'), False, True, 0)
        self.add_accel_group(self._menubar.get_accel_group())

    def _quit_action(self, action, data):
        self.emit('destroy')

    def _close_action(self, action, data):
        self.emit('destroy')

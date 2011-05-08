import gtk
import os.path

import sucker
from DownloadsTab import DownloadsTab
from PluginsDialog import PluginsDialog

class Ui(gtk.Window):
    def __init__(self, engine):
        gtk.Window.__init__(self)

        self.plugin_engine = engine

        self.set_title('Sucker')
        self.resize(400, 400)

        self._box = gtk.VBox()
        self.add(self._box)

        self._setup_menubar()

        self._notebook = gtk.Notebook()
        self._notebook.connect('switch-page', self._notebook_tab_changed)
        self._box.pack_start(self._notebook, True, True, 0)

        self._attach_downloads_tab()
        self._attach_torrents_tab()

    def set_plugin_infos(self, infos):
        self.plugin_infos = infos

    def _setup_menubar(self):
        entries = (
            ('File'   , None           , '_File'   , None     , None, None),
            ('Close'  , gtk.STOCK_CLOSE, None      , '<ctl>w' , None, self._close_action),
            ('Quit'   , gtk.STOCK_QUIT , None      , '<ctl>q' , None, self._quit_action),
            ('Edit'   , None           , '_Edit'   , None     , None, None),
            ('Plugins', None           , '_Plugins', None     , None, self._plugin_action),
            ('Help'   , None           , '_Help'   , None     , None, None),
            ('About'  , gtk.STOCK_ABOUT, None      , None     , None, self._about_action),
        )

        action = gtk.ActionGroup('MenuBarAction')
        action.add_actions(entries)

        ui_file = os.path.join(sucker.DATA_DIR, 'ui', 'menubar.ui')

        self._menubar= gtk.UIManager()
        self._menubar.add_ui_from_file(ui_file)
        self._menubar.insert_action_group(action)

        self._box.pack_start(self._menubar.get_widget('/MenuBar'), False, True, 0)
        self.add_accel_group(self._menubar.get_accel_group())

    def _about_action(self, action):
        authors = (
            'Maintainers:',
            'Ali Vakilzade <ali.vakilzade@gmail.com>',
            'Bersam Karbasion <bersam.k@gmail.com>',
        )

        dialog = gtk.AboutDialog()
        dialog.set_name('Sucker!')
        dialog.set_version(sucker.VERSION)
        dialog.set_comments('It Sucks!')
        dialog.set_copyright('GPLv3')
        dialog.set_license('Blah blah GPLv3 blah blah.\nYou should blah but you can\'t blah.\nIf you had\'nt blah so blah')
        dialog.set_website('https://github.com/aliva/sucker')
        dialog.set_website_label('Homepage')
        dialog.set_authors(authors)
        dialog.run()
        dialog.destroy()
    
    def _quit_action(self, action):
        self.emit('destroy')

    def _close_action(self, action):
        self.emit('destroy')

    def _plugin_action(self, action):
        dialog = PluginsDialog()
        dialog.create_rows(self.plugin_infos)
        dialog.run()
        dialog.destroy()

    def _attach_downloads_tab(self):
        self._downloads_tab = DownloadsTab(self.plugin_engine)
        self._notebook.append_page(self._downloads_tab, gtk.Label("Downloads"))

    def _attach_torrents_tab(self):
        self._torrents_tab = gtk.Label('Torrent')
        self._notebook.append_page(self._torrents_tab, gtk.Label("Torrents"))

    def _notebook_tab_changed(self, notebook, tab, num):
        if num == 0:
            action , string = self._downloads_tab.get_menubar_actiongroup()
            self._menubar.insert_action_group(action, 0)
            id = self._menubar.add_ui_from_string(string)
            self._current_tab_menubar_ui_id  = id
            self._current_tab_menubar_action = action
        else:
            self._menubar.remove_ui(self._current_tab_menubar_ui_id)
            self._menubar.remove_action_group(self._current_tab_menubar_action)

        self._menubar.ensure_update()

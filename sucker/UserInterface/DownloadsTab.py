import gobject
import gtk
import time
import os
from gettext import lgettext as _

import sucker

class DownloadsTab(gtk.VBox):
    def __init__(self, engine):
        gtk.VBox.__init__(self, False, 0)

        self.plugin_engine = engine

        self._setup_menubar()

    def get_menubar_actiongroup(self):
        entries = (
            ('Downloads'  , None         , _("_Downloads")          , None    , None ,None),
            ('NewDownload', gtk.STOCK_ADD, _("_Create New Download"), '<ctl>n', None , self._new_download_action),
        )

        action = gtk.ActionGroup('DownloadsTabAction')
        action.add_actions(entries)

        ui_file = sucker.find_data('ui/downloads-menubar.ui')
        with open(ui_file) as f:
            string = f.read()

        return action, string

    def _setup_menubar(self):
        entries = (
            ('Add', gtk.STOCK_ADD, None, None, None, self._new_download_action),
        )

        action = gtk.ActionGroup('DownloadTabAction')
        action.add_actions(entries)

        ui_file = sucker.find_data('ui/downloads-toolbar.ui')

        self._toolbar = gtk.UIManager()
        self._toolbar.add_ui_from_file(ui_file)
        self._toolbar.insert_action_group(action)

        self.pack_start(self._toolbar.get_widget('/ToolBar'), False, True, 0)
        #self.add_accel_group(self._menubar.get_accel_group())

    def _new_download_action(self, action):
        ui_file = sucker.find_data('ui/downloads-add-dialog.ui')

        builder = gtk.Builder()
        builder.add_from_file(ui_file)

        ok = builder.get_object('ok')
        ok.set_sensitive(False)

        combo = builder.get_object('manager')
        combo.connect('changed', self._add_combo_changed, builder)

        model = gtk.ListStore(gtk.gdk.Pixbuf, gobject.TYPE_STRING)
        combo.set_model(model)

        renderer = gtk.CellRendererPixbuf()
        combo.pack_start(renderer)
        combo.add_attribute(renderer, 'pixbuf', 0)

        renderer = gtk.CellRendererText()
        combo.pack_start(renderer)
        combo.add_attribute(renderer, 'text', 1)

        for info in self.plugin_engine.get_active_infos():
            if 'downloader' in info['type']:
                iter = model.append()
                model.set(iter, 0, None, 1, info['name'])

        dialog = builder.get_object('general')
        dialog.connect('response', self._add_response, builder)
        dialog.run()

    def _add_response(self, dialog, response, builder):
        if response == gtk.RESPONSE_OK:
            combo  = builder.get_object('manager')
            model  = combo.get_model()
            active = combo.get_active()
            manager = model[active][1]

            entry = builder.get_object('url')
            url = entry.get_text()

            dic = {
                'url':url,
                'id' :time.strftime('%y%m%d%H%M%S', time.gmtime())
            }

            self.plugin_engine.add_download(manager, dic)

        dialog.destroy()

    def _add_combo_changed(self, combo, builder):
        model  = combo.get_model()
        active = combo.get_active()
        selected = model[active][1]

        ok = builder.get_object('ok')
        ok.set_sensitive(True)

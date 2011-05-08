import gobject
import gtk
import os
from gettext import lgettext as _

import sucker

class PluginsDialog(gtk.Dialog):
    def __init__(self):
        gtk.Dialog.__init__(self)

        ui_file = sucker.find_data('ui/plugins.ui')

        self.builder = gtk.Builder()
        self.builder.add_from_file(ui_file)
        self.builder.connect_signals(self)

        obj = self.builder.get_object('general')
        box = self.get_content_area()
        box.pack_start(obj, True, True, 0)

        self.setup_treeview()

    def create_rows(self, infos):
        self.infos = infos

        tree  = self.builder.get_object('treeview')
        model = tree.get_model()

        for info in infos:
            iterator = model.append()
            model.set(iterator,
                      0, info['active'],
                      1, info['name'])

    def setup_treeview(self):
        tree = self.builder.get_object('treeview')

        liststore = gtk.ListStore(
                        gobject.TYPE_BOOLEAN,
                        gobject.TYPE_STRING)
        tree.set_model(liststore)

        renderer = gtk.CellRendererToggle()
        renderer.connect('toggled', self._enabled_toggle)
        column = gtk.TreeViewColumn(_("Enabled"), renderer, active=0)
        tree.append_column(column)

        renderer = gtk.CellRendererText()
        column = gtk.TreeViewColumn(_("Plugin"), renderer, text=1)
        tree.append_column(column)

        selection = self.builder.get_object('treeview-selection')
        selection.connect('changed', self._active_row_changed)

    def _active_row_changed(self, selection):
        model, iter = selection.get_selected()

        name = model.get_value(iter, 1)

        for info in self.infos:
            if info['name'] == name:
                break

        label  = self.builder.get_object('plugin_title')
        label.set_markup('<span font="20" size="xx-large">%s</span>' % info['name'])

        label  = self.builder.get_object('description_text')
        label.set_text(info['desc'])

        label  = self.builder.get_object('authors_text')
        label.set_text(info['authors'])

        label  = self.builder.get_object('copyright_text')
        label.set_text(info['copyright'])

        label  = self.builder.get_object('site_text')
        label.set_text(info['website'])

        button = self.builder.get_object('configure_button')
        button.set_sensitive(False)
        

    def _enabled_toggle(self, toggle, path):
        tree  = self.builder.get_object('treeview')
        model = tree.get_model()

        iter  = model.get_iter((int(path),))
        fixed = model.get_value(iter, 0)
        name  = model.get_value(iter, 1)

        fixed = not fixed
        model.set(iter, 0, fixed)

        for info in self.infos:
            if info['name'] == name:
                info['activate_function'](fixed)
                break

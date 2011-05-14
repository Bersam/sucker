import gtk

class statusicon:
    def __init__(self):
        pass

    def activate(self, shell):
        self.window_is_hidden = False
        self.shell = shell

        self.status_icon = gtk.status_icon_new_from_stock(gtk.STOCK_MISSING_IMAGE)
        self.status_icon.connect('activate', self.signal_activate)
        self.status_icon.set_visible(True)

        window = shell.get_window()
        window.connect('delete-event', self.signal_delete_event)

    def deactivate(self, shell):
        self.status_icon.set_visible(False)

        window = shell.get_window()
        window.show_all()

    def signal_activate(self, icon):
        window = self.shell.get_window()

        if self.window_is_hidden:
            window.show()
            self.window_is_hidden = False
        else:
            self.signal_delete_event(window, None)


    def signal_delete_event(self, window, event):
        self.window_is_hidden = True
        window.hide()
        return True

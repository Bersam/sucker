import gtk

class statusicon:
    def __init__(self):
        pass

    def activate(self, shell):
        self.status_icon = gtk.status_icon_new_from_stock(gtk.STOCK_MISSING_IMAGE)
        self.status_icon.set_visible(True)

    def deactivate(self, shell):
        self.status_icon.set_visible(False)

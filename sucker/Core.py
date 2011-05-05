from gi.repository import Gtk

from PluginEngine import Engine
from UserInterface import Ui
from Config import Config

class Core:
    def __init__(self):
        self.ui = Ui()
        self.ui.connect('destroy', Gtk.main_quit)

        self.config = Config()

        self.engine = Engine()
        self.engine.load_plugins()

    def run(self):
        self.ui.show_all()
        Gtk.main()

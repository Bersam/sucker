import gtk

from PluginEngine import Engine
from UserInterface import Ui
from Config import Config

class Core:
    def __init__(self):
        self.config = Config()

        self.engine = Engine()
        self.engine.load_plugins()

        self.ui = Ui(self.engine)
        self.ui.connect('destroy', gtk.main_quit)
        self.ui.set_plugin_infos(self.engine.get_infos())

    def run(self):
        self.ui.show_all()
        gtk.main()

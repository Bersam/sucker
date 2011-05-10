import gtk

from DataBase import DataBase
from PluginEngine import Engine
from UserInterface import Ui
from Config import Config

class Core:
    def __init__(self):
        self.config = Config()

        self.db = DataBase()

        self.engine = Engine(self.db)
        self.engine.load_plugins()

        self.ui = Ui(self.engine, self.db)
        self.ui.connect('destroy', gtk.main_quit)
        self.ui.set_plugin_infos(self.engine.get_infos())

    def run(self):
        self.ui.show_all()
        gtk.main()

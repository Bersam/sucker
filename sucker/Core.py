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

        self.ui = Ui(self.engine, self.config)
        self.ui.connect('destroy', self.quit)
        self.ui.set_plugin_infos(self.engine.get_infos())

        self.engine.set_shell_items(self.ui)
        self.engine.load_plugins()

    def run(self):
        self.ui.show_all()
        gtk.main()

    def quit(self, window):
        self.engine.deactivate_all()
        gtk.main_quit()

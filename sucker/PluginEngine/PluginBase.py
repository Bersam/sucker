import configparser
import imp
import os.path

class PluginBase:
    def __init__(self, path):
        self.error = False
        self.path = path
        tmp, name = os.path.split(path)
        self.infofile = '%s.sucker-plugin' % name

        self._load_infofile()
        self._import_module()

    def __del__(self):
        self.deactivate()

    def activate(self):
        self.plugin_class.activate()

    def deactivate(self):
        self.plugin_class.deactivate()

    def _load_infofile(self):
        infofile = os.path.join(self.path, self.infofile)
        with open(infofile) as f:
                info_str = f.read()
        string = '[DEFAULT]\n' + info_str
        conf = configparser.ConfigParser()
        conf.read_string(string)
        self.info = dict(conf.defaults())
        tmp = self.info['type'].lower().split(',')
        self.info['type'] = [s.strip() for s in tmp]

    def _import_module(self):
        try:
            f, pathname, desc = imp.find_module(self.info['module'], [self.path])
            module = imp.load_module(self.info['name'], f, pathname, desc)
            self.plugin_class = getattr(module, self.info['module'])()
        except ImportError as err:
            print (err)
            self.error = True
        except AttributeError as err:
            print (err)
            self.error = True

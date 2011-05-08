import ConfigParser
import imp
import io
import os.path

class Plugin:
    def __init__(self, path, shell):
        self.error = False
        self.path = path
        tmp, name = os.path.split(path)
        self.infofile = '%s.sucker-plugin' % name

        self.shell = shell

        self._load_infofile()
        self._import_module()

    def __del__(self):
        self.deactivate()

    def activate(self):
        if self.error:
            self._can_not_msg('activate')
        else:
            self.plugin_class.activate(self.shell)
            self.info['active'] = True

    def deactivate(self):
        if self.error:
            self._can_not_msg('deactivate')
        else:
            self.plugin_class.deactivate(self.shell)
            self.info['active'] = False

    def _activate_function(self, value):
        if value:
            self.activate()
        else:
            self.deactivate()

    def _load_infofile(self):
        infofile = os.path.join(self.path, self.infofile)
        with open(infofile) as f:
                info_str = f.read()
        string = '[DEFAULT]\n' + info_str
        conf = ConfigParser.ConfigParser()
        conf.readfp(io.BytesIO(string))
        self.info = dict(conf.defaults())

        tmp = self.info['type'].lower().split(',')
        self.info['type'] = [s.strip() for s in tmp]

        self.info['active'] = False
        self.info['activate_function'] = self._activate_function

    def _import_module(self):
        try:
            f, pathname, desc = imp.find_module(self.info['module'], [self.path])
            module = imp.load_module(self.info['name'], f, pathname, desc)
            self.info['desc'] = module.__doc__ or ''
            self.plugin_class = getattr(module, self.info['module'])()
        except ImportError as err:
            print (err)
            self.error = True
        except AttributeError as err:
            print (err)
            self.error = True

    def _can_not_msg(self, func):
        print('Can not ', func, 'for ', self.info['name'])

import ConfigParser
import imp
import io
import os.path
import signal
from gettext import lgettext as _


class Plugin:
    def __init__(self, path, shell):
        self.path = path
        self.shell = shell

        self.downloads = []
        self.process_ids = []

        self.error = False

        tmp, name = os.path.split(path)
        self.infofile = '%s.sucker-plugin' % name

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

        for pid in self.process_ids:
            if pid == None:
                continue
            try:
                os.kill(pid, signal.SIGQUIT)
            except Exception as err:
                print err

            try:
                os.kill(pid, signal.SIGKILL)
            except Exception as err:
                print err

    def start_download(self, dic):
        try:
            pid = self.plugin_class.start_download(dic)
            self.downloads.append(dic['id'])
            self.process_ids.append(pid)
        except AttributeError as err:
            print _("can't add download. %s Plugin doesn't have start_download function" % self.info['name'])
            print err

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
        conf = ConfigParser.ConfigParser({'website':'', 'copyright':'', 'authors':''})
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
        print _("Can not run function: %s for %s" % (func, self.info['name']))

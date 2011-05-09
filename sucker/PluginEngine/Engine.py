import ConfigParser
import io
import os.path

import sucker
from Plugin import Plugin
from shell import shell

class Engine:
    def __init__(self):
        self.plugins  = {}

    def load_plugins(self):
        info_files = []
        for root in sucker.PLUGIN_DIRS:
            for path in os.listdir(root):
                info_files.append(os.path.abspath(os.path.join(root, path, '%s.sucker-plugin' % path)))

        for info_file in info_files:
            if os.path.isfile(info_file):
                with open(info_file) as f:
                    info_str = f.read()
                info_str  = '[DEFAULT]\n' + info_str
                info_conf = ConfigParser.ConfigParser()
                info_conf.readfp(io.BytesIO(info_str))
                try:
                    plug_path, plug_tail = os.path.split(info_file)
                    plug_name   = info_conf.get('DEFAULT', 'name')
                    plug_type   = info_conf.get('DEFAULT', 'type')
                    plug_module = info_conf.get('DEFAULT', 'module')
                    self.plugins[plug_name] = Plugin(plug_path, shell())
                except ConfigParser.NoOptionError as err:
                    msg = err.message
                    msg = msg[msg.find("'")+1:]
                    msg = msg[:msg.find("'")]
                    print _("Can not load %s plugin from %s." % (path, plug_path))
                    print _("Option `%s` not found in .sucker-plugin file." % msg)

    def get_infos(self):
        infos = [self.plugins[key].info for key in self.plugins]
        return infos

    def get_active_infos(self):
        infos = [self.plugins[key].info for key in self.plugins if self.plugins[key].info['active']==True]
        return infos

    def add_download(self, name, dic):
        self.plugins[name].add_download(dic)

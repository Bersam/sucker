import configparser
import os.path

import sucker

class Engine:
    def __init__(self):
        self.plugins  = {}

    def load_plugins(self):
        info_files = []
        for root in sucker.PLUGIN_DIRS:
            for path in os.listdir(root):
                info_files.append(os.path.join(root, path, '%s.sucker-plugin' % path))

        for info_file in info_files:
            if os.path.isfile(info_file):
                with open(info_file) as f:
                    info_str = f.read()
                info_str = '[DEFAULT]\n' + info_str
                info_conf = configparser.ConfigParser()
                info_conf.read_string(info_str)
                info_dic = {}
                try:
                    plug_path   = os.path.join(root, path)
                    plug_name   = info_conf.get('DEFAULT', 'name')
                    plug_type   = info_conf.get('DEFAULT', 'type')
                    plug_module = info_conf.get('DEFAULT', 'module')
                    from PluginBase import PluginBase
                    p = PluginBase(plug_path)
                    self.plugins[plug_name] = p
                    self.plugins[plug_name].activate()
                except configparser.NoOptionError as err:
                    msg = err.message
                    msg = msg[msg.find("'")+1:]
                    msg = msg[:msg.find("'")]
                    print ('Can not load %s plugin from %s.' % (path, plug_path))
                    print ('Option `%s` not found in .sucker-plugin file.' % msg)

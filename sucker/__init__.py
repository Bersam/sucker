import os.path
import glib
import sys
import xdg.BaseDirectory

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from Core import Core

VERSION = '0.0.1'

ROOT_DIR = os.path.abspath(os.path.join(__file__, '..', '..'))

DATA_DIR  = xdg.BaseDirectory.xdg_data_dirs
DATA_DIR  = [os.path.join(dir, 'sucker') for dir in DATA_DIR]
DATA_DIR.insert(0, os.path.abspath(os.path.join(ROOT_DIR, 'data')))

def find_data(name):
    for dir in DATA_DIR:
        full_address = os.path.join(dir, name)
        if os.path.exists(full_address):
            return full_address
        print full_address

CONFIG_DIR = os.path.join(glib.get_user_config_dir(), 'sucker')
if not os.path.isdir(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

PLUGIN_DIRS = [os.path.join(ROOT_DIR, 'sucker/plugins')]

if os.path.isdir(os.path.join(CONFIG_DIR, 'plugins')):
    PLUGIN_DIRS.append(os.path.join(CONFIG_DIR, 'plugins'))

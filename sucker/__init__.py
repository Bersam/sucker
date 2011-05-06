import os.path
import sys

import glib

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from Core import Core

ROOT_DIR = os.path.abspath(os.path.join(__file__, '..', '..'))
DATA_DIR = os.path.abspath(os.path.join(ROOT_DIR, 'data'))

CONFIG_DIR = os.path.join(glib.get_user_config_dir(), 'sucker')
if not os.path.isdir(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

PLUGIN_DIRS = [os.path.join(ROOT_DIR, 'sucker/plugins')]

if os.path.isdir(os.path.join(CONFIG_DIR, 'plugins')):
    PLUGIN_DIRS.append(os.path.join(CONFIG_DIR, 'plugins'))

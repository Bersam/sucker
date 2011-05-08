#!/usr/bin/env python2
#

from distutils.core import setup
from DistUtilsExtra.command import *
from glob import glob

setup(name="sucker",
        version="0.0.1",
        author="Ali Vakilzade",
        author_email="ali.vakilzade@gmail.com",
        url="https://github.com/aliva/sucker",
        license="GPLv3",
        scripts=['bin/sucker',],
        packages=[
            'sucker',
            'sucker.PluginEngine',
            'sucker.UserInterface',

            'sucker.plugins.helloworld',
            'sucker.plugins.aria2',
            ],

        data_files=[
            ('share/sucker/ui', glob('data/ui/*.ui')),
        ],
        cmdclass = {
            'build' :  build_extra.build_extra,
            'build_i18n' :  build_i18n.build_i18n,
            'build_help' :  build_help.build_help,
            'build_icons' :  build_icons.build_icons
        }
)

#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
GooglePlayDownloader
Copyright (C) 2013   Tuxicoman

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import absolute_import
import os.path
import codecs
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "googleplaydownloader", "version.txt"), "r") as f:
    VERSION = f.read().strip()

with codecs.open(os.path.join(HERE, 'README.txt'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
  name="googleplaydownloader",
	version=VERSION,
	description='Google PlayStore APK downloader',
  long_description=LONG_DESCRIPTION,
	author="Tuxicoman",
	author_email="debian@jesuislibre.net",
	url="http://codingteam.net/project/googleplaydownloader",
	license="AGPL",
  packages=find_packages(),
  entry_points={'gui_scripts': ['googleplaydownloader = googleplaydownloader:start_gui'], },
  install_requires=[
    'protobuf>=2.4',
    'requests>=0.12',
    'ndg-httpsclient',
    'pyasn1',
    'configparser',
  ],
	package_data={'googleplaydownloader': ["version.txt", 'img/icon.ico', "ext_libs/android-checkin/target/android-checkin-1.1-jar-with-dependencies.jar"]}
	)

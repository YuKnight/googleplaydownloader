#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
GooglePlayDownloader
Copyright (C) 2013   Tuxicoman

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

with open("src/version.txt", "r") as f:
  version = f.read()[:-1]

from distutils.core import setup

setup(name="googleplaydownloader",
	version=version,
	description='Google PlayStore APK downloader',
	author="Tuxicoman",
	author_email="debian@jesuislibre.net",
	url="http://codingteam.net/project/googleplaydownloader",
	license="AGPL",
	packages=['googleplaydownloader', 'googleplaydownloader.ext_libs','googleplaydownloader.ext_libs.androguard', 'googleplaydownloader.ext_libs.androguard.core', 'googleplaydownloader.ext_libs.androguard.core', 'googleplaydownloader.ext_libs.androguard.core.bytecodes', 'googleplaydownloader.ext_libs.androguard.core.bytecodes.libdvm', 'googleplaydownloader.ext_libs.googleplay_api', 'googleplaydownloader.ext_libs.android-checkin' ],
	package_dir={'googleplaydownloader' : 'src'},
	package_data={'googleplaydownloader': ["version.txt", 'img/icon.ico'], 'googleplaydownloader.ext_libs.android-checkin' : ["target/android-checkin-1.1-jar-with-dependencies.jar"]}
	)

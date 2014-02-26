GooglePlayDownloader is a graphical software to download APKs from the Google Play store.

I ever wanted to get applications from the Google Play store but didn't like my android AOSP system being tainted by Google root services neither being filed in the Google account database.

The software is based on :
- googleplay-api to interact with Google PlayStore (https://github.com/egirault/googleplay-api/) BSD license
- androguard to read info info from local APKs on disk (http://code.google.com/p/androguard/) LGPL license
These libs are packaged in the ext_libs folder for user convenience but are not part of this project.

The GUI (googleplaydownloader.py) is under AGPL licence (copyright Tuxicoman)

Dependencies are:
- protobuf for messages exchanges with Google PlayStore
- python-requests
- wxpython for the GUI
- python 2.5+
- java (optional but needed for autogeneration of a new AndroiID)

You can install them through your package manager. For example on Debian :
# apt-get install python-protobuf python-wxgtk2.8 python-requests java-common

To launch the software, just do :
$ python googleplaydownloader.py

Enjoy !

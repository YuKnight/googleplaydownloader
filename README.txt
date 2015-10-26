GooglePlayDownloader is a graphical software to download APKs from the Google Play store.

I ever wanted to get applications from the Google Play store but didn't like my android AOSP system being tainted by Google root services neither being filed in the Google account database.

The software is based on :
- googleplay-api to interact with Google PlayStore (https://github.com/egirault/googleplay-api/) BSD license
- androguard to read info info from local APKs on disk (http://code.google.com/p/androguard/) LGPL license
- android-checkin-jb.jar to create AndroiID from Google credentials. (https://github.com/bcopos/android-checkin/) MIT license
These libs are packaged in the src/ext_libs folder for user convenience but are not part of this project.

The GUI (googleplaydownloader.py) is under AGPL licence (copyright Tuxicoman)

  Dependencies are:
  - python-protobuf (>=2.4) for messages exchanges with Google PlayStore
  - python-requests (>=0.12)
  - python-ndg-httpsclient for SSL connections
  - python-pyasn1 for SSL connections
  - python-wxgtk2.8 (>=2.8) for the GUI
  - python 2.5+
  - java (optional but needed for autogeneration of a new AndroiID)

  You can install them through your package manager. For example on Debian :
  # apt-get install python-protobuf python-wxgtk2.8 python-requests java-common python-ndg-httpsclient python-pyasn1

1# method : manual launch

  To launch the software form this folder, just do :
  $ python src/googleplaydownloader.py

2# method : debian package

  Build a debian package (you can also download the prebuild .deb from the website)
  $ build_debian_pachage.sh

  Install it
  # dpkg -i googleplaydownloader.deb

  Solve packages dependencies
  # apt-get install -f

Enjoy !

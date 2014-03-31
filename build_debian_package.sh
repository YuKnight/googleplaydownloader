#!/bin/bash

echo --- Prepare packaging ---
if [ ! -d "packages" ]; then
  mkdir packages
fi

if [ -d "dist" ]; then
  rm -rf dist
fi
echo --- Prepare packaging done ---



echo --- Building python package ---

#source dist
python setup.py sdist --formats=gztar
cp dist/googleplaydownloader-0.5.tar.gz packages/googleplaydownloader-0.5.tar.gz 
#clean
rm MANIFEST

echo --- Building python package done ---



echo --- Building debian package ---

#deb
cd dist
tar -xvzf googleplaydownloader-0.5.tar.gz
mv googleplaydownloader-0.5.tar.gz googleplaydownloader_0.5.orig.tar.gz
cd ..

cp -r debian dist/googleplaydownloader-0.5/debian

cd dist/googleplaydownloader-0.5
dpkg-buildpackage
cd ../..

mv dist/googleplaydownloader_0.5-1_all.deb packages/googleplaydownloader_0.5-1_all.deb

echo --- Building debian package done ---



echo --- Cleaning ---

#clean
rm -rf dist

echo --- Cleaning done ---

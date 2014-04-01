#!/bin/bash
src_version=1.0
package_version=1

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
cp dist/googleplaydownloader-${src_version}.tar.gz packages/googleplaydownloader-${src_version}.tar.gz 
#clean
rm MANIFEST

echo --- Building python package done ---



echo --- Building debian package ---

#deb
cd dist
tar -xvzf googleplaydownloader-${src_version}.tar.gz
mv googleplaydownloader-${src_version}.tar.gz googleplaydownloader_${src_version}.orig.tar.gz
cd ..

cp -r debian dist/googleplaydownloader-${src_version}/debian

cd dist/googleplaydownloader-${src_version}
dpkg-buildpackage
cd ../..

mv dist/googleplaydownloader_${src_version}-${package_version}_all.deb packages/googleplaydownloader_${src_version}-${package_version}_all.deb

echo --- Building debian package done ---



echo --- Cleaning ---

#clean
rm -rf dist

echo --- Cleaning done ---

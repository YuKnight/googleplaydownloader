#!/bin/bash
src_version=$(cat src/version.txt)
package_version=1
software_name="googleplaydownloader"

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
cp dist/${software_name}-${src_version}.tar.gz packages/${software_name}-${src_version}.tar.gz 
#clean
rm MANIFEST

echo --- Building python package done ---



echo --- Building debian package ---

#deb
cd dist
tar -xvzf ${software_name}-${src_version}.tar.gz
mv ${software_name}-${src_version}.tar.gz ${software_name}_${src_version}.orig.tar.gz
cd ..

cp -r debian dist/${software_name}-${src_version}/debian

cd dist/${software_name}-${src_version}
dpkg-buildpackage #-us -uc
cd ../..

mv dist/${software_name}_${src_version}-${package_version}_all.deb packages/${software_name}_${src_version}-${package_version}_all.deb

echo --- Building debian package done ---



echo --- Cleaning ---

#clean
rm -rf dist

echo --- Cleaning done ---

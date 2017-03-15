#!/usr/bin/env bash

set -e

package_version=$1
file_name="blissey-$package_version.zip"
file_path=$(cd "$(dirname "$file_name")"; pwd)/$(basename "$file_name")

# Compress the configuration.
zip -9r $file_name configuration

# Compress the AWS Lambda handler source code.
cd scripts/lambda/
zip -9r $file_path main.py

# Compress the dependencies.
cd ~/virtual-environments/blissey/lib/python2.7/site-packages
# cd ../.virtual-environment/lib/python2.7/site-packages
unzip -o blissey-$package_version-py2.7.egg
rm -r EGG-INFO/
zip -9r $file_path *

cd $(dirname "$file_path")
cp $file_name blissey-latest.zip

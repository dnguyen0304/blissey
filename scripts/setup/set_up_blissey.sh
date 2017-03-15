#!/usr/bin/env bash

# Requirements
# ------------
# Python 2.7.x
# git

set -e

groupadd blissey

mkdir --parents /opt/blissey/
mkdir --parents /var/log/blissey/

cd /opt/blissey/

pip install virtualenv
virtualenv --python=/usr/local/bin/python2.7 .virtual-environment
source .virtual-environment/bin/activate

git clone https://github.com/dnguyen0304/blissey.git .
git checkout tags/latest
pip install --requirement=requirements.txt
python setup.py install

chown --recursive ubuntu:blissey /opt/blissey/
chown --recursive ubuntu:blissey /var/log/blissey/

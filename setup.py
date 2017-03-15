#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'blissey'

    description = 'A personal relationship management (PRM) platform.'
    url = 'https://github.com/dnguyen0304/{}.git'.format(package_name)

    with open('./README.md', 'r') as file:
        long_description = file.read()
    with open('./requirements.txt', 'r') as file:
        install_requires = file.read().splitlines()

    setuptools.setup(name=package_name,
                     version='1.0.0',
                     description=description,
                     long_description=long_description,
                     url=url,
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)

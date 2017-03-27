#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'blissey'

    description = 'A personal relationship management (PRM) platform.'

    with open('./README.md', 'r') as file:
        long_description = file.read()

    install_requires = ['jira==1.0.10',
                        'python-dateutil==2.6.0',
                        'twilio==5.7.0']

    setuptools.setup(name=package_name,
                     version='1.1.0',
                     description=description,
                     long_description=long_description,
                     url='https://github.com/dnguyen0304/blissey.git',
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     classifiers=['Programming Language :: Python :: 2.7'],
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)

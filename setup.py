#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()



setup(
    name='reselpy_randomizer',
    version='0.2',
    description="A simple project that provides methods for the return random data",
    author="Bob Reselman",
    author_email='reselbob@gmail.com',
    url='https://github.com/reselbob/reselpy_randomizer',
    download_url='https://github.com/reselbob/reselpy_randomizer/archive/0.2.tar.gz',
    packages=['reselpy_randomizer'],
    include_package_data=True,
    license="MIT license",
    keywords=['reselpy_randomizer', 'randomizer', 'randomization', 'random'],
    test_suite='tests'
)

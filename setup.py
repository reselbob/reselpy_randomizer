#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='reselpy_randomizer',
    version='0.4',
    description="A simple project that provides methods for the return random data",
    author="Bob Reselman",
    author_email='reselbob@gmail.com',
    url='https://github.com/reselbob/reselpy_randomizer',
    download_url='https://github.com/reselbob/reselpy_randomizer/archive/0.4.tar.gz',
    packages=['reselpy_randomizer'],
    package_dir={'reselpy_randomizer': 'reselpy_randomizer'},
    package_data={'reselpy_randomizer': ['data/*.js']},
    include_package_data=True,
    license="MIT license",
    keywords=['reselpy_randomizer', 'randomizer', 'randomization', 'random'],
    test_suite='tests'
)

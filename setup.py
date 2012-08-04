#!/usr/bin/env python

from setuptools import setup, find_packages

name = "spellchecker"

setup(
    name = name,
    version = "0.2",
    url = "http://silpa.org.in/Spellchecker",
    license = "LGPL-3.0",
    description = "Indian Language Spellchecker Library",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = "This library helps in spellchecking\
of indian languages. This library is far from perfect",
    packages = find_packages('.'),
    package_data = {'.':['spellchecker/dicts']},
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools', 'inexactsearch'],
    zip_safe = False,
    )

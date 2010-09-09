#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import glob
import os
import platform
import re
import sys

if platform.system() == 'FreeBSD':
    man_dir = 'man'
else:
    man_dir = 'share/man'

setup(
    name="bpython-gist",
    version = "0.7.1",
    author = "Robert Anthony Farrell (fork by Kenneth Reitz)",
    author_email = "me@kennethreit.zcom",
    description = "Fancy Interface to the Python Interpreter w/ Gist Integration",
    license = "MIT/X",
    url = "http://www.noiseforfree.com/bpython/",
    long_description = """bpython is a fancy interface to the Python
    interpreter for Unix-like operating systems.""",
    install_requires = [
        'pygments',
        'pyparsing',
    ],
    packages = ["bpython"],
    data_files = [
        (os.path.join(man_dir, 'man1'), ['doc/bpython.1']),
        (os.path.join(man_dir, 'man5'), ['doc/bpythonrc.5']),
        ('share/applications', ['data/bpython.desktop'])
    ],
    entry_points = {
        'console_scripts': [
            'bpython = bpython.cli:main',
        ],
    }
)

# vim: encoding=utf-8 sw=4 ts=4 sts=4 ai et sta

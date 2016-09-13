#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys
import re


# a define the version sting inside the package
# see https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
VERSIONFILE="speedyfx/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(name='speedyfx',
      version=version,
      description='',
      author='Koondal developpers',
      packages=find_packages(),
      include_package_data=True,
     )


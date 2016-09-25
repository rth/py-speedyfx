#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
#from distutils.core import setup
#from distutils.extension import Extension
import numpy as np
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True


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

if sys.platform != 'win32':
    compile_args =  dict( extra_compile_args=['-O2', '-march=native', '-mtune=native'],
                 extra_link_args=['-O2', '-march=native', '-mtune=native'])
else:
    compile_args = {}

libraries = []
if os.name == 'posix':
    libraries.append('m')
    libraries.append('stdc++')
include_dirs= [ np.get_include() ]

ext_modules=[
    Extension("speedyfx._hashing",
             ["speedyfx/_hashing.pyx"],
             libraries=libraries,
             **compile_args),
]


setup(name='speedyfx',
      version=version,
      description='',
      author='',
      cmdclass= {'build_ext': build_ext},
      ext_modules= ext_modules,
      include_dirs=include_dirs,
      packages=find_packages(),
      include_package_data=True,
     )


# conda create -n speedyfx-nskl-env setuptools six cython scipy numpy pytest python=3.5
# conda env remove -n speedyfx-nskl-env

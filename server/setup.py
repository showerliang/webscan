#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='webscan',
      version='0.1',
      description='Webscan core',
      author='Sergio Campos',
      author_email='seocam@seocam.net',
      url='http://code.google.com/p/webscan',
      packages=find_packages(),
      install_requires=['django>=1.0','simplejson']
     )



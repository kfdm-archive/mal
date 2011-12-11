#!/usr/bin/env python

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

import gntp

setup(
	name='mal',
	description='MyAnimeList Library in Python',
	author='Paul Traylor',
	url='http://github.com/kfdm/mal/',
	version='0.1',
	packages=['mal'],
	install_requires=['requests'],
	# http://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Natural Language :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Operating System :: OS Independent',
	],
)

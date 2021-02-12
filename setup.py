# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in new_estate_management/__init__.py
from new_estate_management import __version__ as version

setup(
	name='new_estate_management',
	version=version,
	description='Estate management App for Agents',
	author='ridwan',
	author_email='ridwan.ajibola@manqala.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='auto_multitenancy',
    version=version,
    description='This app automates the site creation from site master doctpye',
    author='New Indictrans Technologies pvt. ltd.',
    author_email='gangadhar.k@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)

#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()
from os import path
from setuptools import setup, find_packages

VERSION = open(path.join(path.dirname(__file__), 'VERSION')).read().strip()

setup(
    name = "django-batchadmin",
    version = VERSION,
    url = "http://code.google.com/p/django-batchadmin/",
    author = "Brian Beck",
    author_email = "exogen@gmail.com",
    license = "MIT License",
    description = "Batch actions in the change list views of your Django admin site.",
    packages = ['batchadmin'],
    include_package_data = True,
    zip_safe = False,
)

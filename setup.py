#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from djangocms_slick_slider/__init__.py"""
    import djangocms_slick_slider

    return djangocms_slick_slider.__version__


version = get_version("djangocms_slick_slider", "__init__.py")

if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="djangocms-slick-slider",
    version=version,
    description="""A Django CMS Slider Plugin with Slick""",
    long_description=readme,
    author="Özer Sahin",
    author_email="info@mathison.ch",
    url="https://github.com/oesah/djangocms-slick-slider",
    packages=[
        "djangocms_slick_slider",
    ],
    include_package_data=True,
    install_requires=[
        "django-cms>=3.4",
        "jsonfield",
        "django-filer",
    ],
    license="MIT",
    zip_safe=False,
    keywords="djangocms-slick-slider",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django CMS :: 3.9",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

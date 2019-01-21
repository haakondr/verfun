# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='verfun',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1',

    description="Verfun is a util for generating a checksum for a python function",

    # The project's main homepage.
    url='https://github.com/haakondr/verfun',

    author='Håkon Drolsum Røkenes',
    author_email="drhaakondr@gmail.com",

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        "pyminifier",
        "astunparse",
    ],
    test_suite='tests',
)

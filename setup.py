#!/usr/bin/env python

"""setup.py: Setup script to install the pipdb library. Allows for easy access without having to move around the core files."""

__author__      = "Fraser King"
__year__        = "2024"
__institution__   = "University of Michigan"

import setuptools

setuptools.setup(
    name="pipdb",
    author="Fraser King",
    author_email="kingfr@umich.edu",
    version="0.0.1",
    description="A simple python package to load and interact with Precipitation Imaging Package (PIP) particle microphysics data.",
    url="https://github.com/frasertheking/pipdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
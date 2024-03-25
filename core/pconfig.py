#!/usr/bin/env python

"""pconfig.py: utility resource for calculating various PSD parameters (e.g., N0, lambda)."""

__author__      = "Fraser King"
__year__        = "2024"
__institution__   = "University of Michigan"

### Data Parse Variables
MAIN_PATH = '/Users/fraserking/Development/pip_processing/data/converted/'

### SITES
ALL_SITES = ['HUR', 'KO1', 'KO2', 'IMP', 'YFB', 'MQT', 'FIN', 'APX', 'HAK', 'KIS', 'NSA']

### Plotting Variables
PSD_MIN = 0.1
PSD_MAX = 10000
VVD_MIN = 0
VVD_MAX = 3
RHO_MIN = 0
RHO_MAX = 1
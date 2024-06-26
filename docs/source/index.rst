Welcome to the pipdb documentation!
===================================

.. image:: logo.png
  :width: 600
  :align: center
  :alt: logo


**pipdb**: is a simple library for interacting with Precipitation Imaging Probe datasets, maintained by `Fraser King <https://frasertheking.com/>`_

.. note::
   Note that this project is currently under active development and these documents may therefore change in time.

GitHub
--------

Project  repository: https://github.com/frasertheking/pipdb


What is this?
--------

This package is a simple query API for parsing, visualizing and performing particle size distribution calculations for Precipitation Imaging Package (PIP) data stored on `DeepBlue <https://deepblue.lib.umich.edu/data/concern/data_sets/kk91fm40r?locale=en>`_. For additional details regadring the processing of the DeepBlue data from raw PIP files into NetCDF-4 format, please see the associated GitHub repository: `PIP_Processing <https://github.com/frasertheking/pip_processing>`_.

This package makes it easy as a user to:

1. Load PIP data from NetCDF into xarray (single day, full year, multi-year).
2. Plot site locations.
3. Extract individual variables of interest.
4. Print general statistics for each of the included dataset variables.
5. Curve fit PSD parameters.
6. Plot PSD variables of interest (1D and 2D).
7. Plot mean PSD variables over time.
8. Separate dataset into rain and snow.
9. Compare between original and adjusted L4-derived products.
10. And more!

This project is currently being used for a journal article submitted to AGU's `Earth and Space Science <https://agupubs.onlinelibrary.wiley.com/journal/23335084>`_

Test in Google Colab
--------

To test the capabilities of this library yourself before installing locally, check out our interactive notebook on Google Colab `here <https://colab.research.google.com/drive/1SH-DZ3o8QwG3DI4Vfwv906p190dYkcyV?usp=sharing>`_.

Contents
--------

``Download``

How to download the package contents to your system


``Installation``

How to install the package


``Datasets``

Where to find and download the PIP data to use the API with


``Functions``

API function defitintion references


``Examples``

Interactive notebooks for using the API on real PIP data


Contact
--------

If you have any questions about using the dataset, please reach out to one of the corresponding authors.

- Fraser King, University of Michigan, kingfr@umich.edu
- Claire Pettersen, University of Michigan

.. toctree::
   :hidden:

   download
   installation
   datasets
   functions
   examples
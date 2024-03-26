Welcome to the pipdb documentation!
===================================

.. image:: logo.png
  :width: 600
  :align: center
  :alt: logo


**pipdb**: is a simple library for interacting with Precipitation Imaging Probe datasets, maintained by `Fraser King <https://frasertheking.com/>`_

.. note::
   Note that this project is currently under active development and these documents may therefore change in time.

What is this?
--------

This package is a simple query API for parsing, visualizing and performing particle size distribution calculations for Precipitation Imaging Package (PIP) data stored on `DeepBlue <https://deepblue.lib.umich.edu/data/concern/data_sets/kk91fm40r?locale=en>`_. For additional details regadring the processing of the DeepBlue data from raw PIP files into NetCDF-4 format, please see the associated GitHub repository: `PIP_Processing <https://github.com/frasertheking/pip_processing>`_.

This package makes it easy as a user to:
#. Load PIP data from NetCDF into xarray (single day, full year, multi-year)
#. Plot site locations
#. Extract individual variables of interest
#. Print general statistics for each of the included dataset variables
#. Curve fit PSD parameters
#. Plot PSD variables of interest (1D and 2D)
#. Plot mean PSD variables over time
#. Separate dataset into rain and snow
#. Compare between original and adjusted L4-derived products
#. And more!

This project is currently being used for a journal article submitted to AGU's `Earth and Space Science <https://agupubs.onlinelibrary.wiley.com/journal/23335084>`_

Test in Google Colab
--------

To test the capabilities of this library yourself before installing locally, check out our interactive notebook on Google Colab `here <https://colab.research.google.com/drive/1SH-DZ3o8QwG3DI4Vfwv906p190dYkcyV?usp=sharing>`_.

Contents
--------

``Download``
How to install the package


``Installation``
How to install the package


``Datasets``
How to install the package


``Functions``
How to install the package


``Examples``
How to install the package


``Applications``
How to install the package

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
   applications
<div align="center">

![logo](https://github.com/frasertheking/pipdb/blob/main/images/logo.jpg?raw=true)

**pipdb**: a simple library for interacting with Precipitation Imaging Probe datasets, maintained by [Fraser King](https://frasertheking.com/)

![build](https://github.com/buttons/github-buttons/workflows/build/badge.svg)
[![DOI](https://zenodo.org/badge/DOI/10.7302/DeepBlue.37yx-9q53.svg)](https://doi.org/10.7302/37yx-9q53) 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

</div>

## What is this?

**pipdb** is a simple query API for parsing, visualizing and performing particle size distribution calculations for Precipitation Imaging Package (PIP) data stored on [DeepBlue](https://deepblue.lib.umich.edu/data/concern/data_sets/kk91fm40r?locale=en). For additional details regadring the processing of the DeepBlue data from raw PIP files into NetCDF-4 format, please see the associated GitHub repository: [PIP_Processing](https://github.com/frasertheking/pip_processing).

This project is currently being used for a journal article submitted to AGU's [Earth and Space Science](https://agupubs.onlinelibrary.wiley.com/journal/23335084).

## Test in Google Colab
To test the capabilities of this library yourself before installing locally, check out our interactive notebook on Google Colab below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1SH-DZ3o8QwG3DI4Vfwv906p190dYkcyV?usp=sharing)

## Installation
To install this package on your system:

1. Clone of this GitHub repository:
   
   ```
   git clone https://github.com/frasertheking/pipdb/
   ```
2. Create a conda environment, and install the required package dependencies using conda:

   ```
   conda env create -f pipdb.yml
   ```
3. Activate the pipdb environment:

   ```
   conda activate pipdb
   ```
4. Install the package so you can use it anywhere on your system:

   ```
   python setup.py install
   ```

## Importing
With the package installed, you can now import it into any of your scripts using:
```
import pipdb
```

## What can it do?
While basic, this API handles the reading and visualizing of many common particle size distribution (PSD) parameters of interest. It loads NetCDF data into a standard xarray.Dataset object that can then be interacted with however you see fit. 

More specifically, this API allows users to eaily:
1. Load PIP data from NetCDF into xarray (single day, full year, multi-year)
2. Plot site locations
3. Extract individual variables of interest
4. Print general statistics for each of the included dataset variables
5. Curve fit PSD parameters
6. Plot PSD variables of interest (1D and 2D)
7. Plot mean PSD variables over time
8. Separate dataset into rain and snow
9. Compare between original and adjusted L4-derived products


## Examples
We include an example interactive notebook in the **examples** folder which shows how to perform each the of aforementioned capabilities for some example data. For example:

Generating daily quicklooks:
![ex1](https://github.com/frasertheking/pipdb/blob/main/images/example1.jpg?raw=true)

Calculating mean statistics:
![ex2](https://github.com/frasertheking/pipdb/blob/main/images/example2.jpg?raw=true)


## Data Sources

A Comprehensive Northern Hemisphere Particle Microphysics Dataset from the Precipitation Imaging Package

The data for this project is hosted online on UM's [DeepBlue repository](https://deepblue.lib.umich.edu/data/concern/data_sets/kk91fm40r?locale=en).

We have collected PIP microphysical data from a variety of measurement locations across the northern hemisphere. Data originally in a proprietary ASCII format has been converted to the more universally recognized NetCDF-4 format for ease of sharing and compatibility within the academic community. The conversion process, undertaken using a combination of bash and Python, ensures broader compatibility with various data analysis tools and platforms. A quality assurance (QA) procedure has been undertaken to ensure the integrity of the data. Post QA, the data is transformed into daily NetCDF-4 files following the Climate and Forecast (CF) conventions (version 1.10) and compressed with a level 2 deflation for optimized file size. Additional details into the data curation process can be found in our journal article publication.

For a brief overview of the data study sites and coverage periods, please see the figure below.
![data overview](https://github.com/frasertheking/pipdb/blob/main/images/fig01.jpg?raw=true)


## Documentation
For additional API documentation, please see our wiki at [LINK].


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Note that, as a living project, code is not as clean as it could (should) be, and unit tests need to be produced in future iterations to maintain stability.


## Authors & Contact

- Fraser King, University of Michigan, kingfr@umich.edu
- Claire Pettersen, University of Michigan
- Brenda Dolan, Colorado State University
- Julia Shates, NASA Jet Propulsion Laboratory
- Derek Posselt, NASA Jet Propulsion Laboratory


## Funding
This project was primarily funded by NASA New (Early Career) Investigator Program (NIP) grant at the [University of Michigan](https://umich.edu).




Datasets
=====

DeepBlue PIP Data Overview
------------

A Comprehensive Northern Hemisphere Particle Microphysics Dataset from the Precipitation Imaging Package

The data for this project is hosted online on the University of Michigan's `DeepBlue repository <https://deepblue.lib.umich.edu/data/concern/data_sets/kk91fm40r?locale=en>`_.

We have collected PIP microphysical data from a variety of measurement locations across the northern hemisphere. Data originally in a proprietary ASCII format has been converted to the more universally recognized NetCDF-4 format for ease of sharing and compatibility within the academic community. The conversion process, undertaken using a combination of bash and Python, ensures broader compatibility with various data analysis tools and platforms. A quality assurance (QA) procedure has been undertaken to ensure the integrity of the data. Post QA, the data is transformed into daily NetCDF-4 files following the Climate and Forecast (CF) conventions (version 1.10) and compressed with a level 2 deflation for optimized file size. Additional details into the data curation process can be found in our journal article publication.

This API was designed to be used with this dataset (which is only a few GBs in size).


Data Packaging & Conversion:
------------

Data originally in a proprietary ASCII format has been converted to the more universally recognized NetCDF-4 format for ease of sharing and compatibility within the academic community. The conversion process, undertaken using a combination of bash and Python, ensures broader compatibility with various data analysis tools and platforms.


Location Details:
------------

- International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE-POP or ICP)
- Olympic Mountains Experiment (OLYMPEX or OLY)
- Haukeliseter (HAK)
- Kiruna (KIS)
- Marquette (MQT)
- Gaylord (APX)
- Finland (FIN)
- North Slope Alaska (NSA)
- NASA Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS or IMP)
- Iqaluit (YFB)


Internal Structure of NetCDF Files:
------------

Spatial & Temporal Variables: Lat/Lon and Time
Data Variable: Contains one of the L3/L4 PIP products
Bin Size Information: bin_centers, bin_edges for different particle diameter bins
Note: Each daily file has exactly 1440 time steps with up to 131 bins for 2D variables. Missing data is marked as NaN. Not all variables exist for all days.


Data Levels & Description:
------------

Level 1 (L1): Raw video data with compressed 8-bit grayscale frames (.pvi format) for 10-minute intervals.

Level 2 (L2): Time-stamped particle tables comprising 36 individual particle characteristics for each hydrometeor.

Level 3 (L3): Derived vertical velocity and particle size distribution tables for each minute.

Level 4 (L4): Estimates of effective density, phase classification, and precipitation rate.


Quality Assurance:
------------

A quality assurance (QA) procedure has been undertaken to ensure the integrity of the data. Post QA, the data is transformed into daily NetCDF-4 files following the Climate and Forecast (CF) conventions (version 1.10) and compressed with a level 2 deflation for optimized file size.


Filename Convention:
------------

The naming convention for the NetCDF files is structured as follows:
XXXYYYYMMDD_**product**.nc

Where:
- XXX: PIP instrument number
- YYYYMMDD: Date (YearMonthDay)

**product** can be one of the following:
- min: L4 precipitation product
- rho: Effective density distributions
- psd: Particle size distributions
- vvd: Vertical velocity distributions


Directory Structure:
------------

* SITE_YEAR/
    * netCDF/
        * adjusted_edensity_lwe_rate/
            * XXXYYYYMMDD_min.nc
        * edensity_distributions/
            * XXXYYYYMMDD_rho.nc
        * particle_size_distributions/
            * XXXYYYYMMDD_psd.nc
        * velocity_distributions/
            * XXXYYYYMMDD_vvd.nc
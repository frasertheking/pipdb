pipdb Functions Documentation
===========================

This documentation provides details for each function available in the API, including their purpose, inputs, outputs, and key features. The functions are categorised by their respective modules for easier user navigation.

pconfig Module
------------
This module doesn't actually contain any additional functions, but is the location of many of the general import statements and global variables used throughout.


pcalc Module
------------
Responsible for calculating various summary statistics and PSD parameters with common curve fitting approaches.

**describe_dataset(ds)**
  Provides statistical summaries for each variable in a dataset, excluding specified 2D variables for readability.

  - **Parameters**: 
    - ``ds``: xarray.Dataset containing the data variables.
  - **Returns**: 
    - Prints statistical summaries to the console.

**get_psd_params(ds)**
  Calculates PSD parameters (N0, lambda) using an exponential fitting function.

  - **Parameters**: 
    - ``ds``: xarray.Dataset object with PSD values and bin centers.
  - **Returns**: 
    - Dictionary with PSD parameters and particle count.

**split_dataset_by_ed_adj(dataset)**
  Splits the dataset based on the condition of ed_adj values to avoid unexpected dimension size changes.

  - **Parameters**: 
    - ``dataset``: xarray.Dataset containing the data.
  - **Returns**: 
    - Tuple with low and high ed_adj datasets.


pplot Module
------------
A helper module for data visualization and quicklook generation.

**plot_precip_data_for_day(ds, site, year, month, day)**
  Generates a 1x5 subplot for precipitation data, with specific visualizations for PSD, VVD, and rho.

  - **Parameters**: 
    - ``ds``: xarray.Dataset with precipitation data.
    - ``site``: Site name.
    - ``year``, ``month``, ``day``: Date details.
  - **Returns**: 
    - None. Saves and displays the plot.

**plot_inverse_exponential(a, b)**
  Plots an exponential decay function over a set number of timesteps.

  - **Parameters**: 
    - ``a``: Intercept term of the exponential function.
    - ``b``: Slope term of the exponential function.
  - **Returns**: 
    - None. Saves and displays the plot.

**plot_distribution_means_with_confidence_intervals(ds)**
  Plots mean values with confidence intervals for specified variables.

  - **Parameters**: 
    - ``ds``: xarray.Dataset containing distribution data.
  - **Returns**: 
    - None. Saves and displays the plot.

**polarCentral_set_latlim(lat_lims, ax)**
  Sets latitude limits for polar central plots.

  - **Parameters**: 
    - ``lat_lims``: Latitude limits.
    - ``ax``: Matplotlib axis.
  - **Returns**: 
    - None. Adjusts the axis in place.

**plot_site(site, ds)**
  Plots a site location on a polar central projection.

  - **Parameters**: 
    - ``site``: Site name.
    - ``ds``: xarray.Dataset with site latitude and longitude.
  - **Returns**: 
    - None. Saves and displays the plot.

**plot_sites(sites)**
  Plots multiple site locations on a single polar central projection.

  - **Parameters**: 
    - ``sites``: Dictionary of site names to xarray.Dataset objects with lat/lon.
  - **Returns**: 
    - None. Saves and displays the plot.

**compare_adjusted_values(ds)**
  Compares original and adjusted values for effective density and precipitation rates.

  - **Parameters**: 
    - ``ds``: xarray.Dataset with data to compare.
  - **Returns**: 
    - None. Saves and displays the comparison plots.

pread Module
------------
A data parsing module to quickly load data from NetCDF into xarray.Dataset objects that can be easily manipulated by the user.

**get_precip_data_for_day(base_dir, site_name, year, month, day)**
  Fetches precipitation data for a specific day and site.

  - **Parameters**: 
    - ``base_dir``, ``site_name``, ``year``, ``month``, ``day``: Details for locating the data.
  - **Returns**: 
    - xarray.Dataset with the requested data.

**get_common_dates(base_dir, file_patterns)**
  Identifies dates common to different data types based on file availability.

  - **Parameters**: 
    - ``base_dir``: Base directory for the data files.
    - ``file_patterns``: Patterns to match data files.
  - **Returns**: 
    - Set of common dates.

**load_single_year_data(base_dir, site_name, year)**
  Loads a year's worth of data for a site, ensuring all data types are present for each date.

  - **Parameters**: 
    - ``base_dir``, ``site_name``, ``year``: Details

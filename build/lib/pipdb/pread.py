#!/usr/bin/env python

"""pread.py: utility resource for interacting with the PIP data in Python."""

__author__      = "Fraser King"
__year__        = "2024"
__institution__   = "University of Michigan"

import xarray as xr
import glob
import os
from functools import reduce


def get_precip_data_for_day(base_dir, site_name, year, month, day):
    """
    Fetch precipitation data for a given site, year, month, and day.
    
    Parameters:
    - site_name: The site name (e.g., "SITE")
    - year: The year (YYYY)
    - month: The month (MM)
    - day: The day (DD)
    
    Returns:
    - An xarray.Dataset containing all data variables for the specified period.
    """
    
    file_patterns = {
        'edensity_lwe_rate': 'adjusted_edensity_lwe_rate/*{year}{month:02d}{day:02d}_min.nc',
        'edensity_distributions': 'edensity_distributions/*{year}{month:02d}{day:02d}_rho.nc',
        'particle_size_distributions': 'particle_size_distributions/*{year}{month:02d}{day:02d}_psd.nc',
        'velocity_distributions': 'velocity_distributions/*{year}{month:02d}{day:02d}_vvd.nc',
    }
    
    dataset = xr.Dataset()
            
    for data_type, pattern in file_patterns.items():
        file_path_pattern = os.path.join(base_dir, pattern.format(year=int(year), month=int(month), day=int(day)))
        files = glob.glob(file_path_pattern)

        if len(files) == 0:
            print(f'Error: No data found for at {site_name} on {year}{month}{day}')
            return
        
        for file in files:
            data = xr.open_dataset(file)
            
            for variable in data.variables:
                if variable not in ['lat', 'lon', 'time']:
                    new_name = f"{data_type}_{variable}" if variable not in ['ed_adj', 'nrr_adj', 'rr_adj'] else variable
                    data = data.rename({variable: new_name})
            
            dataset = xr.merge([dataset, data])
    
    return dataset



def get_common_dates(base_dir, file_patterns):
    """
    Identifies common dates across different data types based on available files.
    
    Parameters:
    - base_dir: Base directory for the data.
    - file_patterns: Dictionary of file patterns for different data types.
    
    Returns:
    - A set of dates (YYYYMMDD) that are common across all data types.
    """

    date_sets = []
    for pattern in file_patterns.values():
        files = glob.glob(os.path.join(base_dir, pattern))
        dates = {os.path.basename(f).split('_')[0] for f in files}
        date_sets.append(dates)
    
    common_dates = set.intersection(*date_sets)
    return common_dates



def load_single_year_data(base_dir, site_name, year):
    
    file_patterns = {
        'edensity_lwe_rate': f'adjusted_edensity_lwe_rate/*.nc',
        'edensity_distributions': f'edensity_distributions/*.nc',
        'particle_size_distributions': f'particle_size_distributions/*.nc',
        'velocity_distributions': f'velocity_distributions/*.nc',
    }
    
    common_dates = get_common_dates(base_dir, file_patterns)
    
    all_data = []
    for date in common_dates:
        daily_data = []
        for data_type, pattern in file_patterns.items():
            specific_pattern = pattern.replace(f'{year}', str(year)).replace('*', date + "*")
            file_path = os.path.join(base_dir, specific_pattern)
            files = glob.glob(file_path)

            if len(files) == 0:
                print(f'Error: No data found for at {site_name} on {year}')
                return
            
            for file in files:
                data = xr.open_dataset(file)
                for variable in data.variables:
                    if variable not in ['lat', 'lon', 'time']:
                        new_name = f"{data_type}_{variable}" if variable not in ['ed_adj', 'nrr_adj', 'rr_adj'] else variable
                        data = data.rename({variable: new_name})
                daily_data.append(data)
        
        if daily_data:
            merged_daily_data = reduce(lambda x, y: xr.merge([x, y]), daily_data)
            all_data.append(merged_daily_data)
    
    if all_data:
        merged_yearly_data = reduce(lambda x, y: xr.concat([x, y], dim='time'), all_data)
        return merged_yearly_data
    else:
        return xr.Dataset()



def load_data_for_sites(main_path, sites_to_include):
    """
    Loads data into xarray datasets for specified sites and allows for easy comparison between sites and years.

    Parameters:
    - main_path: The main directory path where YEAR_SITE subfolders are located.
    - sites_to_include: A list of sites to include in the loading process.

    Returns:
    - A dictionary of xarray datasets keyed by 'YEAR_SITE'.
    """
    
    datasets = {}
    
    year_site_dirs = [d for d in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, d))]
    
    for year_site in year_site_dirs:
        _, site_name = year_site.split('_')
        
        if site_name in sites_to_include:
            year, site = year_site.split('_')
            
            base_dir = os.path.join(main_path, year_site, 'netCDF')
            
            file_patterns = {
                'edensity_lwe_rate': 'adjusted_edensity_lwe_rate/*.nc',
                'edensity_distributions': 'edensity_distributions/*.nc',
                'particle_size_distributions': 'particle_size_distributions/*.nc',
                'velocity_distributions': 'velocity_distributions/*.nc',
            }
            
            common_dates = get_common_dates(base_dir, file_patterns)
            year_data = load_year_data(site, year, base_dir, common_dates, file_patterns)
            
            datasets[f"{year}_{site}"] = year_data
    
    return datasets

def load_year_data(site_name, year, base_dir, common_dates, file_patterns):
    """
    Adjusted version of the previously defined load_year_data to accept base_dir and common_dates directly.
    """

    print("Loading:", site_name, year)
    all_data = []
    for date in common_dates:
        daily_data = []
        for data_type, pattern in file_patterns.items():
            specific_pattern = pattern.replace('*', date + "*")
            file_path = os.path.join(base_dir, specific_pattern)
            files = glob.glob(file_path)

            if len(files) == 0:
                continue 

            for file in files:
                data = xr.open_dataset(file)
                for variable in data.variables:
                    if variable not in ['lat', 'lon', 'time']:
                        new_name = f"{data_type}_{variable}" if variable not in ['ed_adj', 'nrr_adj', 'rr_adj'] else variable
                        data = data.rename({variable: new_name})
                daily_data.append(data)
        
        if daily_data:
            merged_daily_data = reduce(lambda x, y: xr.merge([x, y]), daily_data)
            all_data.append(merged_daily_data)
    
    if all_data:
        merged_yearly_data = reduce(lambda x, y: xr.concat([x, y], dim='time'), all_data)
        return merged_yearly_data
    else:
        return xr.Dataset()
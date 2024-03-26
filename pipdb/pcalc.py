#!/usr/bin/env python

"""pcalc.py: utility resource for calculating various PSD parameters (e.g., N0, lambda)."""

__author__      = "Fraser King"
__year__        = "2024"
__institution__   = "University of Michigan"

import numpy as np
from scipy.optimize import curve_fit


def describe_dataset(ds):
    excluded_vars = ['lat', 'lon', 'edensity_distributions_rho', 'particle_size_distributions_psd', 'velocity_distributions_vvd'] # ignore 2d vars for readability

    print("Dataset statistics:")
    print(f'Site position: ({ds.lat.values}, {ds.lon.values})')
    print()

    for var_name, data_array in ds.data_vars.items():
        if var_name in excluded_vars:
            continue

        mean_val = data_array.mean(dim='time', skipna=True).values
        std_val = data_array.std(dim='time', skipna=True).values
        quantiles = data_array.quantile([0.25, 0.5, 0.75], dim='time', skipna=True).values
        non_nan_count = data_array.count(dim='time').values
        unique_values_count = np.unique(data_array.values[~np.isnan(data_array.values)]).size
        sum_val = data_array.sum(dim='time', skipna=True).values
        data_type = data_array.dtype
        memory_usage = data_array.nbytes

        print(f"{var_name}:")
        print(f"    Mean = {mean_val}, Standard Deviation = {std_val}")
        print(f"    25th Percentile = {quantiles[0]}, Median = {quantiles[1]}, 75th Percentile = {quantiles[2]}")
        print(f"    Non-NaN Count = {non_nan_count}, Unique Values = {unique_values_count}")
        print(f"    Sum = {sum_val}, Data Type = {data_type}")
        print(f"    Memory Usage = {memory_usage} bytes\n")

def get_psd_params(ds):
    psd_values = ds.particle_size_distributions_psd
    bin_centers = ds.particle_size_distributions_bin_centers.values

    func = lambda t, a, b: a * np.exp(-b*t)

    block_avg = np.mean(psd_values[:,:], axis=0)
    valid_indices = ~np.isnan(block_avg)
    valid_bin_centers = bin_centers[valid_indices]

    ret_N0 = 0
    ret_lambda = 0
    try:
        popt, pcov = curve_fit(func, valid_bin_centers, block_avg, p0 = [1e4, 2], maxfev=600)
        if popt[0] > 0 and popt[0] < 10**7 and popt[1] > 0 and popt[1] < 10:
            ret_N0 = popt[0]
            ret_lambda = popt[1]

    except FileNotFoundError:
        print("Could not fit PSD curve with available data.")

    particle_count = int(np.nansum(psd_values[:,:], axis=(0, 1)))
    return {'N0': ret_N0, 'lambda': ret_lambda, 'count': particle_count}


def split_dataset_by_ed_adj(dataset):
    """
    Approach to split the input dataset into two subsets based on the condition
    of ed_adj values, aiming to avoid unexpected dimension size changes.

    Parameters:
    - dataset: xarray.Dataset containing the data.

    Returns:
    - low_ed_adj_dataset: Subset of the dataset where ed_adj values are <= 0.4.
    - high_ed_adj_dataset: Subset of the dataset where ed_adj values are > 0.4.
    """

    low_ed_adj_times = dataset.time.where(dataset.ed_adj <= 0.4, drop=True)
    high_ed_adj_times = dataset.time.where(dataset.ed_adj > 0.4, drop=True)

    snowfall_ds = dataset.sel(time=low_ed_adj_times)
    rainfall_ds = dataset.sel(time=high_ed_adj_times)

    if len(snowfall_ds.time.values) == 0:
        snowfall_ds = None
    if len(rainfall_ds.time.values) == 0:
        rainfall_ds = None

    return (snowfall_ds, rainfall_ds)

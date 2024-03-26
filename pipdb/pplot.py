#!/usr/bin/env python

"""pplot.py: utility resource for plotting PIP variables in Python."""

__author__      = "Fraser King"
__year__        = "2024"
__institution__   = "University of Michigan"

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patheffects as pe
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import LogNorm


def plot_precip_data_for_day(ds, site, year, month, day):
    """
    Plots a 1x5 subplot for the given xarray.Dataset with the first three plots as 2D data using imshow.
    
    Parameters:
    - ds: xarray.Dataset containing the precipitation data.
    """
    fig, axs = plt.subplots(5, 1, figsize=(12, 18), constrained_layout=True)
    fig.suptitle(f'PIP Variable Quicklook for {site} on {year}-{month}-{day}')

    axs[0].patch.set_facecolor('#000871')
    h = axs[0].imshow(ds['particle_size_distributions_psd'].T, cmap='plasma', norm=LogNorm(vmin=0.1, vmax=10000), aspect='auto')
    cbar = fig.colorbar(h, ax=axs[0])
    cbar.set_label('PSD (m$^{−3}$ mm$^{−1}$)')
    bin_centers = ds.particle_size_distributions_bin_centers.values
    ticks_idx = np.linspace(0, len(bin_centers) - 50, 4, dtype=int)
    axs[0].set_yticks(ticks_idx)
    axs[0].set_yticklabels(bin_centers[ticks_idx])
    axs[0].set_ylim((0, 81))
    axs[0].invert_yaxis()
    axs[0].set_xlabel('Minute of day')
    axs[0].set_ylabel('Mean D (mm)')
    axs[0].invert_yaxis()

    axs[1].patch.set_facecolor('#0b0780')
    h = axs[1].imshow(ds['velocity_distributions_vvd'].T, cmap='plasma', vmin=0, vmax=3, aspect='auto')
    cbar = fig.colorbar(h, ax=axs[1])
    cbar.set_label('VVD (m s$^{-1}$)')
    bin_centers = ds.velocity_distributions_bin_centers.values
    ticks_idx = np.linspace(0, len(bin_centers) - 50, 4, dtype=int)
    axs[1].set_yticks(ticks_idx)
    axs[1].set_yticklabels(bin_centers[ticks_idx])
    axs[1].set_ylim((0, 81))
    axs[1].invert_yaxis()
    axs[1].set_xlabel('Minute of day')
    axs[1].set_ylabel('Mean D (mm)')
    axs[1].invert_yaxis()

    axs[2].patch.set_facecolor('white')
    h = axs[2].imshow(ds['edensity_distributions_rho'].T, cmap='seismic', vmin=0, vmax=1, aspect='auto')
    cbar = fig.colorbar(h, ax=axs[2])
    cbar.set_label('Rho (g cm$^{-3}$)')
    bin_centers = ds.edensity_distributions_bin_centers.values
    ticks_idx = np.linspace(0, len(bin_centers) - 50, 4, dtype=int)
    axs[2].set_yticks(ticks_idx)
    axs[2].set_yticklabels(bin_centers[ticks_idx])
    axs[2].set_ylim((0, 81))
    axs[2].invert_yaxis()
    axs[2].set_xlabel('Minute of day')
    axs[2].set_ylabel('Mean D (mm)')
    axs[2].invert_yaxis()

    axs[3].plot(np.arange(1440), ds['ed_adj'], linewidth=2, color='black', label='ed_adj')
    axs[3].set_xlabel('Minute of day')
    axs[3].set_ylabel('Adjusted eDensity (g cm$^{-3}$)')
    axs[3].grid(True)
    axs[3].set_xlim((0, 1440))
    
    axs[4].plot(np.arange(1440), ds['nrr_adj'], linewidth=2, label='Snow', color='r')
    axs[4].plot(np.arange(1440), ds['rr_adj'], linewidth=2, label='Rain', color='b')
    axs[4].set_title('nrr_adj and rr_adj over Time')
    axs[4].set_xlabel('Minute of day')
    axs[4].set_ylabel('LWE Precipitation Rate (mm hr$^{-1}$)')
    axs[4].set_xlim((0, 1440))
    axs[4].legend()
    axs[4].grid(True)

    plt.savefig('../images/precip_for_day.png')
    plt.show()


def plot_inverse_exponential(a, b):
    """
    Plots the exponential decay function a * np.exp(-b * t) over 131 timesteps.

    Parameters:
    - a: Intercept term of the exponential function.
    - b: Slope term of the exponential function.
    """
    t = np.linspace(0, 26.1, 131)
    
    y = a * np.exp(-b * t)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, linewidth=2, color='black', label=f'$\lambda=${round(b, 3)}')
    plt.title('PSD Curve')
    plt.xlabel('Diameter (mm)')
    plt.ylabel('N$_0$ (mm$^{−3}$ mm$^{−1}$)')
    plt.xlim((0, 26.1))
    plt.legend()
    plt.grid(True)
    plt.savefig('../images/psd.png')
    plt.show()


def plot_distribution_means_with_confidence_intervals(ds):
    variables = [
        ('edensity_distributions_rho', 'edensity_distributions_bin_centers', 'Rho (g cm$^{-3}$)', 'Rho'),
        ('particle_size_distributions_psd', 'particle_size_distributions_bin_centers', 'PSD (m$^{−3}$ mm$^{−1}$)', 'PSD'),
        ('velocity_distributions_vvd', 'velocity_distributions_bin_centers', 'VVD (m s$^{-1}$)', 'VVD')
    ]
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    
    for i, (variable_name, bins, units, title) in enumerate(variables):
        means = ds[variable_name].mean(dim='time')
        ci_lower = means - 1.96 * ds[variable_name].std(dim='time') / np.sqrt(len(ds['time']))
        ci_upper = means + 1.96 * ds[variable_name].std(dim='time') / np.sqrt(len(ds['time']))
        
        axs[i].plot(ds[bins], means, label='Mean', linewidth=2, color='black')
        axs[i].fill_between(ds[bins], ci_lower, ci_upper, color='black', alpha=0.2, label='95% CI')
        axs[i].set_title(f'{title} Means')
        axs[i].set_xlabel('Bin Centers')
        axs[i].set_ylabel(units)
        axs[i].legend()
        axs[i].grid(True)
    
    plt.tight_layout()
    plt.savefig('../images/1d_means_with_ci.png')
    plt.show()

def polarCentral_set_latlim(lat_lims, ax):
    ax.set_extent([-180, 180, lat_lims[0], lat_lims[1]], ccrs.PlateCarree())
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax.set_boundary(circle, transform=ax.transAxes)

def plot_site(site, ds):
    plt.figure(figsize=(12, 12))
    ax = plt.axes(projection=ccrs.NorthPolarStereo())
    polarCentral_set_latlim([30, 90], ax)
    ax.stock_img()
    ax.coastlines(resolution='50m', color='black', zorder=1001)
    ax.gridlines(linewidth=3, color='gray', linestyle=':', alpha=0.5, zorder=1005) 
    ax.add_feature(cfeature.LAND)
    plt.title('Site location - ' + site + f': ({ds.lat.values}, {ds.lon.values})')
    plt.scatter(ds.lon.values, ds.lat.values, color='black', marker='o', edgecolors='white', linewidth=4, s=500, transform=ccrs.Geodetic(), zorder=1006)  
    plt.savefig('../images/site_location.png')
    plt.show()

def plot_sites(sites):
    plt.figure(figsize=(12, 12))
    ax = plt.axes(projection=ccrs.NorthPolarStereo())
    polarCentral_set_latlim([30, 90], ax)
    ax.stock_img()
    ax.coastlines(resolution='50m', color='black', zorder=1001)
    ax.gridlines(linewidth=3, color='gray', linestyle=':', alpha=0.5, zorder=1005) 
    ax.add_feature(cfeature.LAND)
    plt.title('Multi-Site Location Plot')

    for k, v in sites.items():
        plt.scatter(v.lon.values, v.lat.values, color='black', marker='o', edgecolors='white', linewidth=4, s=500, transform=ccrs.Geodetic(), zorder=1006)  
        plt.text(v.lon.values[0] + 3, v.lat.values[0] + 3, k, fontsize=20, color='black', path_effects=[pe.withStroke(linewidth=8, foreground="white")], transform=ccrs.Geodetic(), zorder=1007)

    plt.savefig('../images/multi_site_locations.png')
    plt.show()

def compare_adjusted_values(ds):
    comparisons = [
        (None, None, None, None, None, None),
        ('edensity_lwe_rate_rr', 'rr_adj', 'black', 'Rainfall Rates', 'Original (m s$^{-1}$)', 'Adjusted (m s$^{-1}$)'),
        ('edensity_lwe_rate_nrr', 'nrr_adj', 'black', 'Snowfall Rates', 'Original (m s$^{-1}$)', 'Adjusted (m s$^{-1}$)')
    ]

    rho_vals = np.where(ds['edensity_distributions_rho'] == 0, np.nan, ds['edensity_distributions_rho'])
    rho_means = np.nanmean(rho_vals, axis=1)
    
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    
    count = 0
    for ax, (var1, var2, var3, var4, var5, var6) in zip(axes, comparisons):
        ax.grid()
        if count == 0:
            ax.scatter(ds['edensity_lwe_rate_ed'], rho_means, color='red', alpha=0.5, label='Original')
            ax.scatter(ds['ed_adj'], rho_means, color='blue', alpha=0.5, label='Adjusted')
            ax.set_title('Original vs. Adjusted Effective Density')
            ax.set_xlim(0, 0.4)
            ax.set_ylim(0, 0.4)
            ax.set_xlabel('L4 Effective Density (g cm$^{-3}$)')
            ax.set_ylabel('Rho (g cm$^{-3}$)')
            ax.legend()
            ax.plot([0, 0.4], [0, 0.4], linestyle='--', linewidth=2, color='black')
        else:
            ax.scatter(ds[var1], ds[var2], color=var3, alpha=0.5)
            ax.set_title(f'{var1} vs. {var2}')
            ax.set_xlabel(var5)
            ax.set_ylabel(var6)
            ax.set_xlim(0, np.nanmax(ds[var1]))
            ax.set_ylim(0, np.nanmax(ds[var1]))
            ax.set_title(var4)
            ax.plot([0, np.max(ds[var1])], [0, np.max(ds[var1])], linestyle='--', linewidth=2, color='black')
        count += 1
    
    plt.tight_layout()
    plt.savefig('../images/adjusted_values_comparisons.png')
    plt.show()
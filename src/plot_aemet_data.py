#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:58:15 2025

@author: israelale
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import numpy as np

def plot_aemet_data(df):
    """
    Create a 2x2 plot of the main meteorological variables
    
    Args:
        df: DataFrame with AEMET data (with date as index)
    """
    if len(df) == 0:
        print("No data available for plotting")
        return
    
    # Create figure and subplots
    fig, ax = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('AEMET Meteorological Data', fontsize=16)
    
    # Prepare the x-axis (dates)
    nticks = 10
    t = pd.date_range(start=df.index.min(), end=df.index.max(), periods=nticks)
    fmt = mdates.DateFormatter('%d/%m/%Y')
    
    # 1. Temperature (top left)
    if 'tmed' in df.columns and 'tmin' in df.columns and 'tmax' in df.columns:
        ax[0,0].plot(df.index, df['tmed'], '-r', linewidth=2, label='Mean')
        ax[0,0].plot(df.index, df['tmin'], '-b', linewidth=1, label='Minimum')
        ax[0,0].plot(df.index, df['tmax'], '-g', linewidth=1, label='Maximum')
        ax[0,0].set_xticks(t)
        ax[0,0].set_xticklabels(t, rotation=60)
        ax[0,0].xaxis.set_major_formatter(fmt)
        ax[0,0].set_ylabel('Temperature (°C)')
        ax[0,0].set_title('Air Temperature')
        ax[0,0].legend()
        ax[0,0].grid(True, linestyle='--', alpha=0.7)
    
    # 2. Precipitation (top right)
    if 'prec' in df.columns:
        ax[0,1].bar(df.index, df['prec'], color='blue', alpha=0.7, width=1)
        ax[0,1].set_xticks(t)
        ax[0,1].set_xticklabels(t, rotation=60)
        ax[0,1].xaxis.set_major_formatter(fmt)
        ax[0,1].set_ylabel('Precipitation (mm)')
        ax[0,1].set_title('Daily Precipitation')
        if df['prec'].max() > 0:
            ax[0,1].set_yticks(np.linspace(0, df['prec'].max(), 10))
        ax[0,1].grid(True, linestyle='--', alpha=0.7)
    
    # 3. Atmospheric Pressure (bottom left)
    if 'presMax' in df.columns and 'presMin' in df.columns:
        ax[1,0].plot(df.index, df['presMax'], '-r', label='Maximum')
        ax[1,0].plot(df.index, df['presMin'], '-b', label='Minimum')
        ax[1,0].set_xticks(t)
        ax[1,0].set_xticklabels(t, rotation=60)
        ax[1,0].xaxis.set_major_formatter(fmt)
        ax[1,0].set_ylabel('Pressure (hPa)')
        ax[1,0].set_title('Atmospheric Pressure')
        ax[1,0].legend()
        ax[1,0].grid(True, linestyle='--', alpha=0.7)
    
    # 4. Wind Speed (bottom right)
    if 'velmedia' in df.columns:
        ax[1,1].plot(df.index, df['velmedia'], '-', color='green', label='Mean')
        if 'racha' in df.columns:
            ax[1,1].plot(df.index, df['racha'], '--', color='orange', alpha=0.7, label='Gusts')
        ax[1,1].set_xticks(t)
        ax[1,1].set_xticklabels(t, rotation=60)
        ax[1,1].xaxis.set_major_formatter(fmt)
        ax[1,1].set_ylabel('Speed (km/h)')
        ax[1,1].set_title('Wind Speed')
        ax[1,1].legend()
        ax[1,1].grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout and show
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()
    
    return fig
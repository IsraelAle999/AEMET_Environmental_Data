#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:02:28 2025

@author: israelale
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def monthly_analysis(df):
    """
    Perform basic monthly analysis of meteorological data
    
    Args:
        df: DataFrame with AEMET data (with date as index)
    """
    if len(df) == 0:
        print("No data available for analysis")
        return

    # Create figure for monthly plots
    fig, ax = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Monthly Analysis of Meteorological Data', fontsize=16)
    
    # 1. Monthly average temperature (top left)
    if 'tmed' in df.columns:
        monthly_temp = df['tmed'].resample('M').mean()
        monthly_temp_min = df['tmin'].resample('M').mean()
        monthly_temp_max = df['tmax'].resample('M').mean()
        
        ax[0,0].plot(monthly_temp.index, monthly_temp, '-ro', linewidth=2, markersize=8, label='Mean')
        ax[0,0].plot(monthly_temp_min.index, monthly_temp_min, '-bo', linewidth=1, markersize=6, label='Minimum')
        ax[0,0].plot(monthly_temp_max.index, monthly_temp_max, '-go', linewidth=1, markersize=6, label='Maximum')
        ax[0,0].set_ylabel('Temperature (°C)')
        ax[0,0].set_title('Monthly Average Temperature')
        ax[0,0].legend()
        ax[0,0].grid(True, linestyle='--', alpha=0.7)
        fmt_months = mdates.DateFormatter('%b %Y')
        ax[0,0].xaxis.set_major_formatter(fmt_months)
        for label in ax[0,0].get_xticklabels():
            label.set_rotation(45)
    
    # 2. Monthly total precipitation (top right)
    if 'prec' in df.columns:
        monthly_prec = df['prec'].resample('M').sum()
        
        ax[0,1].bar(monthly_prec.index, monthly_prec, color='blue', alpha=0.7, width=20)
        ax[0,1].set_ylabel('Precipitation (mm)')
        ax[0,1].set_title('Monthly Total Precipitation')
        ax[0,1].grid(True, linestyle='--', alpha=0.7)
        ax[0,1].xaxis.set_major_formatter(fmt_months)
        for label in ax[0,1].get_xticklabels():
            label.set_rotation(45)
    
    # 3. Rainy days per month (bottom left)
    if 'prec' in df.columns:
        # Count days with precipitation > 0
        rain_days = df['prec'] > 0
        monthly_rain_days = rain_days.resample('M').sum()
        
        ax[1,0].bar(monthly_rain_days.index, monthly_rain_days, color='skyblue', alpha=0.7, width=20)
        ax[1,0].set_ylabel('Number of Days')
        ax[1,0].set_title('Rainy Days per Month')
        ax[1,0].grid(True, linestyle='--', alpha=0.7)
        ax[1,0].xaxis.set_major_formatter(fmt_months)
        for label in ax[1,0].get_xticklabels():
            label.set_rotation(45)
    
    # 4. Monthly average wind speed (bottom right)
    if 'velmedia' in df.columns:
        monthly_wind = df['velmedia'].resample('M').mean()
        
        ax[1,1].plot(monthly_wind.index, monthly_wind, '-o', color='green', markersize=8)
        ax[1,1].set_ylabel('Speed (km/h)')
        ax[1,1].set_title('Monthly Average Wind Speed')
        ax[1,1].grid(True, linestyle='--', alpha=0.7)
        ax[1,1].xaxis.set_major_formatter(fmt_months)
        for label in ax[1,1].get_xticklabels():
            label.set_rotation(45)

    # Adjust layout and show
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()

    return fig
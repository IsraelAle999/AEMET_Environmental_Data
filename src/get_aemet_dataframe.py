#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:55:46 2025

@author: israelale
"""

from src.split_date_range import split_date_range
import time
import pandas as pd

def get_aemet_dataframe(aemet_client, start_date, end_date, station_id):
    """
    Retrieve AEMET data and return it as a pandas DataFrame
    with the date as the index and all variables as columns
    """
    # Split the date range into subranges of up to 6 months
    date_ranges = split_date_range(start_date, end_date)
    
    all_data = []
    
    # Make a request for each subrange
    for i, (sub_start, sub_end) in enumerate(date_ranges):
        print(f"Retrieving data for range {i+1}/{len(date_ranges)}: {sub_start} to {sub_end}")
        
        try:
            # Pause between requests to avoid overloading the API
            if i > 0:
                time.sleep(2)
                
            # Make the API request
            datos_rango = aemet_client.get_valores_climatologicos_diarios(sub_start, sub_end, station_id)
            
            if datos_rango:
                all_data.extend(datos_rango)
            else:
                print(f"No data found for range {sub_start} to {sub_end}")
        
        except Exception as e:
            print(f"Error retrieving data for range {sub_start} to {sub_end}: {str(e)}")
    
    # If no data, return an empty DataFrame
    if not all_data:
        print("No data found for the requested range.")
        return pd.DataFrame()
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Convert dates and set as index
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df = df.sort_values('fecha')
    
    # Process numeric data (replace commas with dots)
    # Precipitation
    df['prec'] = df['prec'].replace(['Ip'], '0.0', regex=True)
    df['prec'] = df['prec'].replace([','], '.', regex=True).astype('float', errors='ignore')
    
    # Other numeric columns
    numeric_columns = ['tmin', 'tmax', 'tmed', 'presMax', 'presMin', 'velmedia', 'racha', 'sol']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].replace([','], '.', regex=True).astype('float', errors='ignore')
    
    # Set date as index for the final DataFrame
    df_final = df.set_index('fecha')
    
    # Display information about the created DataFrame
    print(f"DataFrame created with {len(df_final)} records from {df_final.index.min().strftime('%Y-%m-%d')} to {df_final.index.max().strftime('%Y-%m-%d')}")
    print(f"Available columns: {df_final.columns.tolist()}")
    
    return df_final
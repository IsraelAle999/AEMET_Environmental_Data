# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:06:03 2023

@author: israelale
"""

from aemet import Aemet

from src.get_aemet_dataframe import get_aemet_dataframe
from src.monthly_analysis import monthly_analysis
from src.plot_aemet_data import plot_aemet_data

#########################################################################################
# Create API keys with this link: https://opendata.aemet.es/centrodedescargas/obtencionAPIKey
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpc3JhZWxhMDQyQGdtYWlsLmNvbSIsImp0aSI6IjVkNGJiOTA0LTYwMTQtNGI4Yi1hOGExLTE1OGEyNDliNmQzMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzQ1OTMyOTY1LCJ1c2VySWQiOiI1ZDRiYjkwNC02MDE0LTRiOGItYThhMS0xNThhMjQ5YjZkMzMiLCJyb2xlIjoiIn0.ejgsIgDmj8iDmKUNAwVx23GIoNy6pAOBPNtyqaWsShM"
aemet_client = Aemet(api_key=API_KEY)
#########################################################################################

if __name__ == "__main__":
    # Query parameters
    Start_date = '2022-01-01T00:00:00UTC'
    Final_date = '2023-01-01T23:59:59UTC'  # Any time range is valid
    Station_ID = '5530E'   # Find station at https://opendata.aemet.es/centrodedescargas/productosAEMET?
    
    # Retrieve data as DataFrame
    df_aemet = get_aemet_dataframe(aemet_client, Start_date, Final_date, Station_ID)
    
    # Show first rows
    print("\nFirst rows of the DataFrame:")
    print(df_aemet.head())
    
    # Generate plots
    plot_aemet_data(df_aemet)
    
    # Monthly analysis
    monthly_analysis(df_aemet)
    
    # Additional analysis examples
    
    # 1. Basic statistics for mean temperature
    if 'tmed' in df_aemet.columns:
        print("\nMean temperature statistics:")
        print(df_aemet['tmed'].describe())
    
    # 2. Monthly average temperature
    if 'tmed' in df_aemet.columns:
        print("\nMonthly average temperature:")
        monthly_temp = df_aemet['tmed'].resample('M').mean()
        print(monthly_temp)
    
    # 3. Monthly total precipitation
    if 'prec' in df_aemet.columns:
        print("\nMonthly total precipitation:")
        monthly_prec = df_aemet['prec'].resample('M').sum()
        print(monthly_prec)
    
    # 4. Hottest days in the period
    if 'tmax' in df_aemet.columns:
        print("\nHottest days:")
        hottest_days = df_aemet.sort_values('tmax', ascending=False).head(5)
        print(hottest_days[['tmax', 'tmin', 'tmed']])
    
    # 5. Rainiest days in the period
    if 'prec' in df_aemet.columns:
        print("\nRainiest days:")
        rainiest_days = df_aemet.sort_values('prec', ascending=False).head(5)
        print(rainiest_days[['prec', 'tmed']])

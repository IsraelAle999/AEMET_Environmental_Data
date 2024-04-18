# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:06:03 2023

@author: enriq
"""
import pandas as pd
import json
from pandas import json_normalize
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import time
from aemet import Aemet
import numpy as np

#########################################################################################

# Create api_keys with this link  https://opendata.aemet.es/centrodedescargas/obtencionAPIKey

aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpc3JhZWxhMDQyQGdtYWlsLmNvbSIsImp0aSI6ImNkZTE1ZTc0LTBjOTEtNDEyNC04MGZiLTEyM2FmNDRhYWUwMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA3MzAzMDQ1LCJ1c2VySWQiOiJjZGUxNWU3NC0wYzkxLTQxMjQtODBmYi0xMjNhZjQ0YWFlMDMiLCJyb2xlIjoiIn0.b0SHmauJbxv7-fdgsPDxNupf1DVnCsN4Wrzz2Bxi5x0')

#########################################################################################

Start_date = '2022-01-01T00:00:00UTC'
Final_date = '2024-02-01T23:59:59UTC'
Station_ID = '5530E'   # Buscar estacion en esta pagina https://opendata.aemet.es/centrodedescargas/productosAEMET?
datos = aemet_client.get_valores_climatologicos_diarios(Start_date, Final_date, Station_ID);
datajson = json.dumps(datos, indent=2)


#########################################################################################

f = open('newfile.json', "w")
f.write(datajson)
f.close()

df = pd.read_json (r'newfile.json')
df.to_csv (r'Final.csv', index = None)

dfp = pd.read_csv(r'Final.csv', decimal=",")
dfp.time = pd.to_datetime(dfp['fecha'], format='%Y-%m-%d') # %H:%M:%S.%f


nticks = 10
t = pd.date_range(start=dfp.time[0],
                  end=dfp.time[len(dfp.time)-1],
                  periods=nticks)
fmt = mdates.DateFormatter('%d/%m/%Y')

#########################################################################################

fig, ax = plt.subplots(2,2)
ax[0,0].plot(dfp.time, dfp['tmed'],'-r',linewidth=2)
ax[0,0].plot(dfp.time, dfp['tmin'],'-b',linewidth=1)
ax[0,0].plot(dfp.time, dfp['tmax'],'-b',linewidth=1)
ax[0,0].set_xticks(t)
ax[0,0].set_xticklabels(t,rotation=60)
ax[0,0].xaxis.set_major_formatter(fmt)
ax[0,0].title.set_text('Air Temperature [Celsius]')

dfp['prec'] = dfp['prec'].replace(['Ip'], '0.0', regex=True)
dfp['prec'] = dfp['prec'].replace([','], '.', regex=True).astype('float')
ax[0,1].plot(dfp.time, dfp['prec'])
ax[0,1].set_xticks(t)
ax[0,1].set_xticklabels(t,rotation=60)
ax[0,1].xaxis.set_major_formatter(fmt)
ax[0,1].set_yticks(np.linspace(dfp['prec'].min(),dfp['prec'].max(),10))
ax[0,1].title.set_text('Precipitation [mm]')

ax[1,0].plot(dfp.time, dfp['presMax'],'-r')
ax[1,0].plot(dfp.time, dfp['presMin'],'-b')
ax[1,0].set_xticks(t)
ax[1,0].set_xticklabels(t,rotation=60)
ax[1,0].xaxis.set_major_formatter(fmt)
ax[1,0].title.set_text('Air Pressure [hPa]')

ax[1,1].plot(dfp.time, dfp['velmedia'])
ax[1,1].set_xticks(t)
ax[1,1].set_xticklabels(t,rotation=60)
ax[1,1].xaxis.set_major_formatter(fmt)
ax[1,1].title.set_text('Wind speed [km/h]')
fig.show()
plt.tight_layout()

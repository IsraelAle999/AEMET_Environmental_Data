# AEMET Meteorological Data Extraction and Analysis

This repository provides Python utilities to fetch historical climatological data from the AEMET OpenData API, process it with pandas, and visualize it using matplotlib.

---

## Contents

- **api_keys**: Configuration of the AEMET API access token.
- [split_date_range.py](src/split_date_range.py): Function to split a date range into up to 6‑month subranges to comply with API limitations.
- [get_aemet_dataframe.py](src/get_aemet_dataframe.py): Fetches daily climatological values and returns them as a pandas DataFrame.
- [plot_aemet_data.py](src/plot_aemet_data.py): Generates a 2×2 plot for temperature, precipitation, pressure, and wind.
- [monthly_analysis.py](src/monthly_analysis.py): Performs monthly analyses (means, totals, and day counts) and visualizes them.
- **main**: Example script demonstrating parameter usage for date range and station ID.

---

## Instructions for use

1. Create api_keys with this link [AEMET](https://opendata.aemet.es/centrodedescargas/obtencionAPIKey).
2. Generate de api key. Example:

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpc3JhZWxhMDQyQGdtYWlsLmNvbSIsImp0aSI6ImNkZTE1ZTc0LTBjOTEtNDEyNC04MGZiLTEyM2FmNDRhYWUwMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA3MzAzMDQ1LCJ1c2VySWQiOiJjZGUxNWU3NC0wYzkxLTQxMjQtODBmYi0xMjNhZjQ0YWFlMDMiLCJyb2xlIjoiIn0
```
3. Search for the station ID on the web:  [Station_ID](https://opendata.aemet.es/centrodedescargas/productosAEMET?).
4. Define the Start and Final date in ```main.py``` file.
5. Run the ```main.py``` file

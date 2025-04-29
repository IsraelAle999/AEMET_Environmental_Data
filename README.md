# AEMET Meteorological Data Extractor & Analyzer

A Python toolkit to seamlessly retrieve, process, and visualize historical climatological data from the AEMET OpenData API.

---

## 🚀 Features

- **Flexible Data Retrieval**: Fetch daily temperature, precipitation, pressure, and wind data for any weather station.
- **Automatic Date Splitting**: Breaks long date ranges into 6‑month intervals to comply with API limits.
- **Pandas Integration**: Clean and ready-to-analyze `DataFrame` output.
- **Visualization**: Predefined 2×2 plot for quick insights and customizable charts.
- **Monthly Analysis**: Compute monthly means, totals, and record day counts at a glance.
- **Extensible Examples**: `main.py` script demonstrates common use cases.

---

## 📦 Requirements

- Python **3.12+**
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [aemet](https://pypi.org/project/aemet/)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

1. **Obtain an API Key**:
   - Go to the [AEMET OpenData portal](https://opendata.aemet.es/centrodedescargas/obtencionAPIKey) and generate your token.
2. **Store your key**:
   - Create a file named `api_keys.py` at the project root containing:
     ```python
     API_KEY = "your_api_token_here"
     ```

---

## 🗂️ Project Structure

```          # Your AEMET API credentials
├── main.py                  # Example script showing usage      # Project dependencies
└── src
    ├── split_date_range.py  # Split long date ranges into subranges
    ├── get_aemet_dataframe.py # Fetch and assemble DataFrame
    ├── plot_aemet_data.py   # Create 2×2 climatology plots
    └── monthly_analysis.py  # Compute and visualize monthly stats
```

---

## ▶️ Usage

1. **Edit `main.py`**:
   ```python
   from aemet import Aemet
   from api_keys import API_KEY
   from src.get_aemet_dataframe import get_aemet_dataframe
   from src.plot_aemet_data import plot_aemet_data
   from src.monthly_analysis import monthly_analysis

   # Initialize client
   aemet_client = Aemet(api_key=API_KEY)

   # Define query parameters
   Start_date  = '2022-01-01T00:00:00UTC'
   Final_date  = '2023-01-01T23:59:59UTC'
   Station_ID  = '5530E'  # Look up station IDs on AEMET portal

   # Fetch data
   df = get_aemet_dataframe(aemet_client, Start_date, Final_date, Station_ID)

   # Inspect and visualize
   print(df.head())
   plot_aemet_data(df)
   monthly_analysis(df)
   ```
2. **Run the script**:
   ```bash
   python main.py
   ```

You’ll see console output of the first rows and monthly summaries, as well as pop‑up plots showing temperature, precipitation, pressure, and wind trends.

---

## 🛠️ Custom Analysis

In `main.py`, you can add examples such as:

```python
# 1. Descriptive stats for mean temperature
df['tmed'].describe()

# 2. Resampled monthly averages
monthly_temp = df['tmed'].resample('M').mean()
print(monthly_temp)

# 3. Rainiest days in the period
rainiest_days = df.nlargest(5, 'prec')
print(rainiest_days[['fecha', 'prec', 'tmed']])
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please fork the repo and open a pull request.

---


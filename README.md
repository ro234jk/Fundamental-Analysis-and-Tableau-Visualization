# Fundamental-Analysis-and-Tableau-Visualization


## Overview
This project is designed to perform **fundamental analysis** of the **NIFTY Top 100 stocks**. It fetches key financial metrics for these companies, organizes the data sector-wise, and visualizes insights such as average PE ratios, dividend yields, and more.

---

## Features
- **Automated Data Collection**: Retrieves financial metrics such as Market Cap, PE Ratio, PB Ratio, EPS, ROE, Dividend Yield, and Debt-to-Equity using the `yfinance` library.
- **Sector-Wise Analysis**: Organizes stocks into sectors for aggregated insights.
- **Visualization**: Generates plots like bar charts for metrics (e.g., average PE ratio by sector).
- **Tableau Integration**: Exports data for further analysis and advanced visualization in Tableau.
- **CSV Export**: Saves the collected data for future use.

---

## Prerequisites
- Python 3.x
- Libraries:
  - `pandas`
  - `yfinance`
  - `matplotlib`

---

## Data Source
- **Stock List**: Ensure a valid dataset containing NIFTY Top 100 stocks, including columns for:
  - `Symbol`: Stock ticker
  - `Sector`: Sector classification

- Example dataset sources:
  - [NSE Website](https://www.nseindia.com)
  - CSV files or online tables with NIFTY 100 data

---

## Usage

### 1. Install Required Libraries
```bash
pip install pandas yfinance matplotlib
```

### 2. Run the Script
- Modify the `nifty_stocks_url` variable to point to your data source.
- Run the script:
```bash
python nifty_fundamental_analysis.py
```

### 3. Output
- The script generates:
  - A **CSV file** containing fundamental data: `NIFTY100_FundamentalData.csv`
  - Visualizations of financial metrics.
  - Export-ready datasets for Tableau visualization.

---

## Key Functions

### `get_fundamental_data(symbol)`
- Fetches financial metrics for a given stock ticker using `yfinance`.

### Sector-Wise DataFrames
- Dynamically creates DataFrames for each unique sector in the dataset.

### Visualization
- Generates bar charts, such as average PE ratios by sector.

---

## Tableau Visualization

### Exporting Data to Tableau
1. Run the script to generate `NIFTY100_FundamentalData.csv`.
2. Open Tableau and connect to the CSV file.
3. Create advanced visualizations such as:
   - Sector-wise PE ratios
   - Market capitalization distribution
   - Comparative analysis of financial metrics

### Example Visualization in Tableau
- **Dashboard**: Combine charts like bar plots and scatter plots to show sector-wise financial health.
- **Filters**: Add interactive filters for sectors, market caps, or PE ratios.

---

## Example Visualization
- **Bar Chart**: Average PE Ratio by Sector

```python
plt.bar(sector_pe_ratios.keys(), sector_pe_ratios.values())
plt.title("Average PE Ratio by Sector (NIFTY 100)")
plt.xlabel("Sector")
plt.ylabel("Average PE Ratio")
plt.show()
```

---

## To-Do
- Add more financial metrics (e.g., Net Profit Margin, Free Cash Flow).
- Automate regular updates using a scheduler.
- Expand visualization options (e.g., line charts for trends).

---

## Troubleshooting
- **Error fetching data**: Ensure the stock ticker is valid and accessible via `yfinance`.
- **Empty Dataset**: Verify the `nifty_stocks_url` or data source is correct.

---

## License
This project is open-source and available under the MIT License.

---




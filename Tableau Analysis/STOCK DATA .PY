import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Load NIFTY Top 100 stock data
# Replace with a valid dataset source containing NIFTY 100 companies
nifty_stocks_url = 'https://example.com/nifty-top-100-stocks'  # Replace with actual source
wiki_page_table = pd.read_html(nifty_stocks_url)
df = wiki_page_table[0]  # Assuming the first table contains the required data

# Display basic data
print("NIFTY Top 100 Stock Data:")
print(df.head())

# Extract the list of stock symbols
stock_symbols = df["Symbol"].tolist()  # Assuming 'Symbol' contains stock tickers
print(f"\nTotal Stocks: {len(stock_symbols)}")

# Function to fetch fundamental data for a stock
def get_fundamental_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            "Symbol": symbol,
            "Market Cap": info.get("marketCap"),
            "PE Ratio": info.get("trailingPE"),
            "PB Ratio": info.get("priceToBook"),
            "EPS": info.get("trailingEps"),
            "ROE": info.get("returnOnEquity"),
            "Dividend Yield": info.get("dividendYield"),
            "Debt-to-Equity": info.get("debtToEquity")
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Collect fundamental data for all stocks
fundamental_data = []
for symbol in stock_symbols:
    data = get_fundamental_data(symbol)
    if data:
        fundamental_data.append(data)

# Convert the data to a pandas DataFrame
fundamental_df = pd.DataFrame(fundamental_data)

# Save to CSV for future use
fundamental_df.to_csv("NIFTY100_FundamentalData.csv", index=False)

# Display the collected fundamental data
print("\nCollected Fundamental Data:")
print(fundamental_df.head())

# Example: Analyze sector-wise data (requires 'Sector' column in the dataset)
df_copy = df.copy()
df_copy = df_copy.merge(fundamental_df, on="Symbol")
unique_sectors = df_copy["Sector"].unique()
sector_data = {}
for sector in unique_sectors:
    sector_data[sector] = df_copy[df_copy["Sector"] == sector]

# Example Plot: Average PE Ratio by Sector
sector_pe_ratios = {
    sector: sector_data[sector]["PE Ratio"].mean() for sector in sector_data
}
plt.figure(figsize=(10, 5))
plt.bar(sector_pe_ratios.keys(), sector_pe_ratios.values())
plt.title("Average PE Ratio by Sector (NIFTY 100)")
plt.xlabel("Sector")
plt.ylabel("Average PE Ratio")
plt.xticks(rotation=45)
plt.grid()
plt.show()

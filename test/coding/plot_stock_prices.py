# filename: plot_stock_prices.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Get the current year to fetch year-to-date data
current_year = datetime.now().year
start_date = f"{current_year}-01-01"

# Fetching data for NVDA and TSLA
nvda = yf.download('NVDA', start=start_date)
tsla = yf.download('TSLA', start=start_date)

# Calculate the percentage change in the 'Adj Close' price from the start of the year
nvda_pct_change = (nvda['Adj Close'].pct_change() + 1).cumprod() - 1
tsla_pct_change = (tsla['Adj Close'].pct_change() + 1).cumprod() - 1

# Create a dataframe for plotting
df = pd.DataFrame({'NVDA': nvda_pct_change, 'TSLA': tsla_pct_change})

# Plot the chart
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['NVDA'] * 100, label='NVIDIA', color='blue')
plt.plot(df.index, df['TSLA'] * 100, label='TESLA', color='red')
plt.title(f'NVDA vs TSLA YTD Stock Price Change (%)')
plt.xlabel('Date')
plt.ylabel('YTD Change (%)')
plt.legend()
plt.grid(True)
plt.show()
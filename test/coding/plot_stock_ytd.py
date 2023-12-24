# filename: plot_stock_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Starting date for YTD data
start_date = f"{current_year}-01-01"

# Fetch historical stock data for NVDA and TSLA
nvda_data = yf.download('NVDA', start=start_date, progress=False)
tesla_data = yf.download('TSLA', start=start_date, progress=False)

# Calculate the percentage change from the first available data point
nvda_ytd = (nvda_data['Close'] / nvda_data['Close'].iloc[0] - 1) * 100
tesla_ytd = (tesla_data['Close'] / tesla_data['Close'].iloc[0] - 1) * 100

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(nvda_ytd, label='NVDA YTD')
plt.plot(tesla_ytd, label='TSLA YTD')
plt.title('YTD Stock Price Change for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.show()
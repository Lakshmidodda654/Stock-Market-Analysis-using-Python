import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and date range for analysis
stock_symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"

# Fetch stock data using Yahoo Finance API
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data["Daily_Returns"] = stock_data["Adj Close"].pct_change()

# Calculate cumulative returns
stock_data["Cumulative_Returns"] = (1 + stock_data["Daily_Returns"]).cumprod()

# Plotting stock price and returns
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(stock_data["Adj Close"])
plt.title("Stock Price")
plt.ylabel("Price (USD)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(stock_data["Daily_Returns"])
plt.title("Daily Returns")
plt.ylabel("Returns")
plt.grid(True)

plt.tight_layout()
plt.show()

# Print summary statistics
print("\nSummary Statistics:")
print(stock_data[["Adj Close", "Daily_Returns"]].describe())
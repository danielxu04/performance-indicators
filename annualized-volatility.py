# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/27/2023
# Description: A program that implements annualized volatility calculations
#   for tickers AMZN, GOOG, AAPL (for daily volatility)
# Annualized Volatility:
#   - SD * sqrt(252), where SD is the standard deviation of the percent
#       change series of the Adjusted Close
# --------------------------------------------------------

# Import libraries
import yfinance as yf
import numpy as np

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

def annualized_daily_volatility(df):
    temp = df.copy()
    temp['Returns'] = df['Adj Close'].pct_change()
    vty = temp['Returns'].std() * np.sqrt(252)
    return vty

for t in tickers:
    data = yf.download(t, period='7mo', interval='1d') # 1 day candlestick
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    print('Annualized volatility by day for {} is {}%.'.format(s, annualized_daily_volatility(stock_data[s]) * 100))
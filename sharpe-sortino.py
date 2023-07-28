# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/28/2023
# Description: A program that implements Sharpe and Sortino Ratio calculations
#   for tickers AMZN, GOOG, AAPL
# Sharpe Ratio:
#   (Expected Returns - Risk Free ROR) / SD of Asset Returns
# Sortino Ratio:
#   (Expected Returns - Risk Free ROR) / SD of Negative Asset Returns
# 
# NOTE: These calculations have a fixed 3.9% Risk Free ROR, an approximation 
#   derived from the current 10-year US Treasury bond yield as of July 2023
# --------------------------------------------------------

# Import libraries
import yfinance as yf
import pandas as pd
import numpy as np

# CAGR - takes in a DataFrame and computes the Compounded Average Growth Rate
def cagr(df):
    temp = df.copy()
    temp['Return'] = temp['Adj Close'].pct_change()
    temp['Cumulative Returns'] = (1 + temp['Return']).cumprod()
    # decimal expression of years, based on number of trading days
    n = len(temp)/252
    CAGR = (temp['Cumulative Returns'][-1])**(1/n) - 1
    return CAGR
# ANNUALIZED_DAILY_VOLATILITY - takes in a DataFrame and calculates the Annualized 
#   daily volatility
def annualized_daily_volatility(df):
    temp = df.copy()
    temp['Returns'] = df['Adj Close'].pct_change()
    vty = temp['Returns'].std() * np.sqrt(252)
    return vty

# SHARPE - takes in DataFrame and Risk Free Rate of Return, returns sharpe ratio
def sharpe(df, rfr):
    shp = (cagr(df) - rfr) / annualized_daily_volatility(df)
    return shp

# SORTINO - takes in DataFrame and Risk Free Rate of Return, returns sortino ratio
def sortino(df, rfr):
    temp = df.copy()
    # Calculate STRICTLY negative asset standard deviation
    temp['Return'] = temp['Adj Close'].pct_change()
    negative_returns = np.where(temp['Return'] < 0, temp['Return'], 0)
    negative_volatility = pd.Series(negative_returns[negative_returns != 0]).std() * np.sqrt(252)
    return (cagr(temp) - rfr) / negative_volatility
    
    
# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='7mo', interval='1d') # 1 day candlestick
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    print('The Sharpe Ratio for {} is {}.'.format(s, sharpe(stock_data[s], 0.039)))
    print('The Sortino ratio for {} is {}.'.format(s, sortino(stock_data[s], 0.039)))
    
# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/28/2023
# Description: A program that implements Maximum Drawdown and Calmar Ratio
#   for tickers AMZN, GOOG, AAPL
# --------------------------------------------------------

# Import libraries
import yfinance as yf

# MAX_DRAWDOWN - returns the maximum drawdown of a 7 month period of our analyzed stocks
def max_drawdown(df):
    temp = df.copy()
    temp['Return'] = temp['Adj Close'].pct_change()
    temp['Cumulative Return'] = (1 + temp['Return']).cumprod()
    temp['Cumulative Rolling Max'] = temp['Cumulative Return'].cummax()
    temp['Drawdown'] = temp['Cumulative Rolling Max'] - temp['Cumulative Return']
    md = (temp['Drawdown'] / temp['Cumulative Rolling Max']).max()
    return md

# CAGR - takes in a DataFrame and computes the Compounded Average Growth Rate
def cagr(df):
    temp = df.copy()
    temp['Return'] = temp['Adj Close'].pct_change()
    temp['Cumulative Returns'] = (1 + temp['Return']).cumprod()
    # decimal expression of years, based on number of trading days
    n = len(temp)/252
    CAGR = (temp['Cumulative Returns'][-1])**(1/n) - 1
    return CAGR

# CALMAR - returns the Calmar Ratio for a 7 month period, 1 day candlestick period
#   of analyzed stocks
def calmar(df):
    temp = df.copy()
    calmar_ratio = cagr(temp) / max_drawdown(temp)
    return calmar_ratio

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='7mo', interval='1d') # 1 day candlestick
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    print('Max Drawdown of {} is {}.'.format(s, max_drawdown(stock_data[s])))
    print('Calmar Ratio of {} is {}.\n'.format(s, calmar(stock_data[s])))
    
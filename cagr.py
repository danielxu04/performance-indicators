# --------------------------------------------------------
# Author: Daniel Xu
# Date: 07/20/2023
# Description: A program that implements Compounded Average Growth Rate
#   for AMZN, AAPL, and GOOG
# --------------------------------------------------------

# Import libraries
import yfinance as yf

# CAGR - takes in a DataFrame and computes the Compounded Average Growth Rate
def cagr(df):
    temp = df.copy()
    temp['Return'] = temp['Adj Close'].pct_change()
    temp['Cumulative Returns'] = (1 + temp['Return']).cumprod()
    # decimal expression of years, based on number of trading days
    n = len(temp)/252
    CAGR = (temp['Cumulative Returns'][-1])**(1/n) - 1
    
    return CAGR

# Download historical data for various stocks
tickers = ['AMZN', 'AAPL', 'GOOG']
stock_data = {}

for t in tickers:
    data = yf.download(t, period='7mo', interval='1d') # 1 day candlestick
    data.dropna(how='any', inplace=True)
    stock_data[t] = data
    
for s in stock_data:
    print('{} CAGR calculation: {}'.format(s, cagr(stock_data[s])))
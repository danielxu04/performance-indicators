# Key Performance Indicators for Backtesting and Performance Measurement

Key Performance Indicators (KPIs) and Backtesting are crucial when developing trading strategies, as they measure expected performance of a strategy by testing it on historical data, which hypothetically mimicks real-world trading conditions. It assumes that historical performance forecasts future performance; however, aspects such as slippage, trading cost, brokerage, and stop loss are usually not accounted for. In this repository, we will delve deeper into the realm of KPIs, taking a look at various popular performance indicators:
- Compound Annual Growth Rate (CAGR)
- Annualized Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Calmar Ratio
<br />

## 1. CAGR - Compounded Annual Growth Rate (CAGR)

Compounded Annual Growth Rate is a measurement of the anunaul rate of return realized by assets to reach its current market value from initial value. The calculation is as follows, and assumes the profits are continuously reinvested:
```math
CAGR = \left[ {v_f } \over { v_i} \right]^{1 \over t} - 1
```
where v<sub>i</sub> is initial value, v<sub>f</sub> is final value, and t is expressed in years. <br /><br />
Due to the generality of CAGR, it is versatile and easy to use with different trading strategies. Moreover, since it doesn't reflect investment risk, it is generally good practice to use CAGR alongside a volatility indicator.
<br /><br />

## 2. Annualized Volatility

Let's preface this performance indicator by mentioning that the volatility of a strategy is represented by the standard deviation of the returns on investment. It strives to capture the variability of returns from the mean return. Annualized Volatility, or annualization, is calculated by multiplying volatility with the square root of the annualization factor. 
- **Annualization for daily volatility:**
```math
\sigma * \sqrt252
```
as there are ~252 trading days in a year.
- **Annualization for weekly volatility:**
```math
\sigma * \sqrt52
```
since there are 52 trading weeks in a year.
- **Annualization for monthly volatility:**
```math
\sigma * \sqrt12
```
as we have 12 trading months in a year.<br /><br />
Although volatility is a widely used measure of risk, it is important to consider that it is sometimes inaccurate due to the assumption of a normal distribution of returns, and thus, does not capture tail risk. 



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

Compounded Annual Growth Rate is a measurement of the annual rate of return realized by assets to reach its current market value from initial value. The calculation is as follows, and assumes the profits are continuously reinvested:
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
<br /><br />

## 3. Sharpe Ratio & Sortino Ratio

**Sharpe ratio** is one of the most widely used methods for measuring risk-adjusted relative returns. More specifically, it is the average return in excess of the risk free rate, per unit of volatility. Investors generally pay close attention to this performance metric when comparing funds. <br /><br />
A Sharpe ratio of >1 is considered good, >2 considered very good, and >3 is excellent. It is calculated as follows: <br />
```math
Sharpe \space Ratio = {{R_p - R_f} \over \sigma_p}
```
$R_p =$ Expected Returns <br />
$R_f =$ Risk Free rate of return <br />
$\sigma_p =$ Standard Deviation of Asset Returns<br /><br />

On the other hand, **Sortino ratio** is a variation of Sharpe ratio, which only takes into account the standard deviation of negative returns. It originated from one of the criticisms Sharpe ratio faced - the inability to distinguish between upside and downside fluctuation. Sortino makes that distinction, only considering harmful volatility. It corresponds to the Sharpe ratio calculation with just one small change:
```math
Sortino \space Ratio = {{R_p - R_f} \over \sigma_n}
```
$R_p =$ Expected Returns <br />
$R_f =$ Risk Free rate of return <br />
$\sigma_n =$ Standard Deviation of **Negative** Asset Returns<br /><br />

## 4. Maximum Drawdown & Calmar Ratio

**Maximum Drawdown** refers to a crucial performance metric that centers on the largest percentage decline experienced by an asset's price during a specified time horizon. More precisely, it represents the extent between the highest peak and the lowest trough on the line graph, depicting the price fluctuations of the respective asset, wherein the trough must occur subsequent to the peak.<br /><br />
Given the proclivity for greater volatility and variability in investments subjected to lengthier backtesting periods, it becomes imperitive to be cautious while undertaking comparisons among different investment options. One must ensure the congruity of the maximum drawdown periods. <br /><br />
The **Calmar Ratio** emerges as a consequential ratio derived from the drawdown aanlysis. The ratio gauges the relationship between the CAGR and the Maximum Drawdown. Serving as a measure of risk-adjusted returns, the Calmar Ratio is computed through the following expression:<br />
```math
Calmar \space Ratio = {{Compounded \space Annual \space Return} \over {Maximum \space Drawdown}}
```

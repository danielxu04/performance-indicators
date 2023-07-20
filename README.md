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

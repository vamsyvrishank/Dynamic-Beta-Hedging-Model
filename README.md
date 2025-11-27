
This project implements a complete framework for constructing, analyzing, and dynamically rebalancing a beta-hedged portfolio to offset exposure to a large single-stock position—in this case, Apple (AAPL).

## Dynamic Beta Hedging: The Theoretical Framework

This document outlines the core financial theory behind constructing and managing a dynamically beta-hedged portfolio. The primary goal is to neutralize the systematic market risk of a single stock position, thereby isolating its specific risk and return (alpha).

### 1. What is Beta (β)?

Beta is a fundamental concept in finance that measures the volatility, or systematic risk, of a security or a portfolio in comparison to the market as a whole. Systematic risk is the risk inherent to the entire market that cannot be diversified away.

*   **Beta = 1.0**: The asset's price is expected to move in line with the market.
*   **Beta > 1.0**: The asset is more volatile than the market. For every 1% move in the market, the asset is expected to move more than 1%.
*   **Beta < 1.0**: The asset is less volatile than the market.
*   **Beta = 0**: The asset's movement is uncorrelated with the market.
*   **Negative Beta**: The asset tends to move in the opposite direction of the market.

#### Calculation

Beta is calculated using a linear regression. It is the slope of the line obtained by regressing the returns of the asset (`Ra`) against the returns of a market benchmark (`Rm`), like the S&P 500.

The formula for Beta is:

```
β = Cov(Ra, Rm) / Var(Rm)
```

Where:
*   `Cov(Ra, Rm)` is the covariance of the asset's returns and the market's returns.
*   `Var(Rm)` is the variance of the market's returns.

### 2. What is Hedging?

Hedging is a risk management strategy employed to offset potential losses in an investment. The core idea is to take an opposing position in a related asset.

### 3. Beta Hedging: Neutralizing Market Risk

Beta hedging is a strategy that aims to reduce or eliminate the systematic risk (beta) of a portfolio. If you hold a long position in a stock (e.g., you own shares of Apple, AAPL), you are exposed to the risk that the entire market could decline, taking your stock down with it, regardless of the company's individual performance.

To hedge this risk, an investor can take an offsetting position, typically by short-selling a broad market index ETF (like SPY for the S&P 500). The goal is to create a **"beta-neutral"** portfolio, where the overall portfolio's value is theoretically unaffected by broad market movements.

#### How to Construct the Hedge

The amount of the market index to short is determined by the beta of the stock you are hedging.

**Hedge Ratio:** The value of the short position should be equal to the value of your long stock position multiplied by its beta.

*   **Hedge Amount = Value of Stock Position × Beta of the Stock**

For instance, if you hold $100,000 worth of a stock with a beta of 1.3, you would need to short $130,000 of a market index ETF to make your position beta-neutral.

### 4. The "Dynamic" Component: Rolling Beta

A stock's beta is not a static, unchanging number. It evolves over time due to changes in the company's business, market sentiment, and overall economic conditions. A "static hedge," where the position is hedged once and then left alone, will quickly become ineffective.

This is why a **dynamic** approach is necessary.

#### Rolling Beta

Instead of calculating a single beta over a long historical period, a **rolling beta** is used. This is calculated by performing the beta regression on a moving window of data (e.g., the past 60, 120, or 252 trading days). This provides a time series of beta values, showing how the asset's sensitivity to the market changes over time.

#### Portfolio Rebalancing

Dynamic beta hedging involves periodically adjusting the hedge based on the most recent rolling beta calculation. This process is called **rebalancing**.

The rebalancing process involves:
1.  **Recalculating Beta**: At regular intervals (e.g., daily, weekly, or monthly), calculate the new rolling beta of your stock position.
2.  **Updating Position Values**: Note the current market value of your stock position.
3.  **Adjusting the Hedge**: Based on the new beta and new stock value, calculate the new target short position in the market index.
4.  **Executing Trades**: Place trades to increase or decrease your short position to match this new target.

This ensures that the portfolio remains as close to beta-neutral as possible over time.

### 5. Project Implementation and Analysis

A successful project will involve simulating and comparing the performance of different portfolio strategies.

#### Key Steps:

1.  **Data Acquisition**: Collect historical daily price data for the target stock (e.g., AAPL) and a market benchmark ETF (e.g., SPY).
2.  **Rolling Beta Calculation**:
    *   Calculate daily returns for both assets.
    *   Implement a function to calculate the beta over a rolling window (e.g., 1-year).
3.  **Portfolio Simulation**:
    *   **Unhedged Portfolio**: Simulate the performance of simply holding the stock.
    *   **Statically Hedged Portfolio**: Calculate the beta at the start of the period. Determine the initial hedge and hold both positions without rebalancing.
    *   **Dynamically Hedged Portfolio**: Simulate the rebalancing process. At each period (e.g., end of the month), recalculate the rolling beta and adjust the short position in the market index accordingly.
4.  **Performance Analysis**:
    *   Compare the three portfolios on key metrics:
        *   **Total Return**: The overall gain or loss.
        *   **Volatility (Standard Deviation)**: The degree of price fluctuation.
        *   **Sharpe Ratio**: Risk-adjusted return.
        *   **Maximum Drawdown**: The largest peak-to-trough decline.

#### Expected Outcome

The hypothesis is that the **dynamically hedged portfolio** will exhibit significantly lower volatility and a smaller maximum drawdown compared to the unhedged portfolio. While the total return may be lower (as you are hedged against market upswings as well as downswings), the risk-adjusted return should be superior, demonstrating the effectiveness of isolating the stock's alpha from the market's beta.


import yfinance as yf
import pandas as pd
import numpy as np
import os

def download_and_process_data():
    """
    Downloads historical data for specified tickers, calculates daily log returns,
    and saves the result to a CSV file.
    """
    # --- 1. Define Tickers and Date Range ---
    # Stock to be hedged
    stock_ticker = 'AAPL'
    
    # Market benchmark
    market_ticker = 'SPY'
    
    # Investment universe for the hedge basket
    universe_tickers = ['FXE', 'EWJ', 'GLD', 'QQQ', 'SHV', 'DBA', 'USO', 'XBI', 'ILF', 'EPP', 'FEZ']
    
    # Combine all tickers into a single list
    all_tickers = [stock_ticker, market_ticker] + universe_tickers
    
    # Define the date range
    start_date = '2024-01-01'
    end_date = '2025-03-01' # Use March 1st to ensure Feb 28th data is included

    # --- 2. Download Historical Data ---
    print(f"Downloading adjusted close prices for {len(all_tickers)} tickers...")
    adj_close_prices = yf.download(all_tickers, start=start_date, end=end_date)['Close']
    print("Download complete.")

    # --- 3. Calculate Daily Log Returns ---
    # Log returns are preferred for time-series analysis
    log_returns = np.log(adj_close_prices / adj_close_prices.shift(1))

    # --- 4. Clean Data ---
    # Remove all rows with any missing values to ensure data alignment across all assets
    cleaned_returns = log_returns.dropna()
    
    # --- 5. Save Data to File ---
    # Create the 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        
    output_path = 'data/daily_returns.csv'
    cleaned_returns.to_csv(output_path)
    
    print(f"Successfully processed data for {len(cleaned_returns)} trading days.")
    print(f"Daily returns saved to '{output_path}'")

if __name__ == '__main__':
    download_and_process_data()


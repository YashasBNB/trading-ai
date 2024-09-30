import MetaTrader5 as mt5
import pandas as pd
import os
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize MT5
def initialize_mt5():
    if not mt5.initialize():
        logging.error("MT5 initialization failed")
        return False
    logging.info("MT5 initialized successfully")
    return True

# Fetch and save live data
def fetch_live_data(symbol, interval=60):
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 1000)  # Fetch last 1000 M1 data points
    if rates is None:
        logging.error(f"Failed to fetch data for {symbol}")
        return

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')  # Convert timestamp
    df.to_csv(f'data/{symbol}_data.csv', index=False)
    logging.debug(f"Data saved for {symbol} to data/{symbol}_data.csv")

# Main function to fetch data
def main():
    symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "NZDUSD", "USDCHF"]
    for symbol in symbols:
        fetch_live_data(symbol)
        time.sleep(1)  # Wait a second between fetches

    mt5.shutdown()  # Clean up MT5

if __name__ == "__main__":
    if initialize_mt5():
        main()

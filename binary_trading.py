import logging
from trading_bot import TradingBot
import json

def main():
    # Load the configuration file
    with open("config.json", "r") as f:
        config = json.load(f)

    # Initialize the trading bot
    bot = TradingBot(config, trade_type="binary")
    
    # Start the trading process
    bot.run_binary_trading()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

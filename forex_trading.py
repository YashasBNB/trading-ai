# forex_trading.py
import json
from trading_bot import TradingBot
from utils import load_config

def main():
    # Load the configuration
    config = load_config("config.json")

    # Create the TradingBot instance for Forex Trading
    bot = TradingBot(config, trade_type="forex")

    # Run the bot's forex trading logic
    bot.run_forex_trading()

if __name__ == "__main__":
    main()

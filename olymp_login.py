import logging
import json
from trading_bot import TradingBot

def main():
    logging.basicConfig(level=logging.INFO)
    config_path = 'config.json'

    with open(config_path) as config_file:
        config = json.load(config_file)

    bot = TradingBot(config, trade_type="binary")
    bot.run_binary_trading()

if __name__ == "__main__":
    main()

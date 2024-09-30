import json
from trading_bot import TradingBot

def main():
    config_path = 'config.json'
    with open(config_path) as config_file:
        config = json.load(config_file)

    bot = TradingBot(config)

    if bot.initialize():
        bot.run()

if __name__ == "__main__":
    main()

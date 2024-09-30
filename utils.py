# utils.py
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def log_message(message):
    logging.info(message)

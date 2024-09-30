import time
from iqoptionapi.stable_api import IQ_Option

# Initialize your IQ Option credentials
email = "yashasnaidu3@gmail.com"  # Replace with your IQ Option email
password = "King@2005"  # Replace with your IQ Option password

# Create an IQ Option instance and log in
iq = IQ_Option(email, password)
iq.connect()

# Check if the connection was successful
if not iq.check_connect():
    print("Failed to connect to IQ Option")
else:
    print("Successfully connected to IQ Option")

# Function to check balance
def check_balance():
    try:
        balance = iq.get_balance()  # Get account balance (as a float)
        if balance is not None:
            print(f"Balance: {balance}")
        else:
            print("Failed to fetch balance.")
    except Exception as e:
        print(f"Error fetching balance: {e}")

# Function to fetch trade history
def get_trade_history():
    try:
        # Fetch trade history (recent trades based on lookback period)
        current_time = int(time.time() * 1000)  # Current Unix timestamp in milliseconds
        lookback_period = 60 * 60 * 1000  # 1 hour in milliseconds (adjust as needed)
        start_time = current_time - lookback_period
        status, history = iq.get_position_history_v2("digital", 50, offset=0, start=start_time, end=current_time)
        
        if status and history:  # Check if fetching was successful
            print(f"Fetched {len(history['positions'])} trades.")
            for trade in history['positions']:
                print(f"Trade ID: {trade['id']}, Status: {trade['status']}, Profit: {trade['close_profit']}")
        else:
            print("No trade history found within the lookback period.")
    except Exception as e:
        print(f"Error fetching trade history: {e}")

# Function to place a trade for binary options
def place_trade(asset, direction, amount, expiry_time):
    try:
        # Place a trade (binary options, use buy_digital_spot)
        check, trade_id = iq.buy_digital_spot(asset, amount, direction, expiry_time)
        if check:
            print(f"Trade placed successfully. Trade ID: {trade_id}")
        else:
            print("Failed to place trade.")
            # Check for specific error messages
            last_error = iq.get_last_error()
            if last_error:
                print(f"Error message: {last_error}")
    except Exception as e:
        print(f"Error placing trade: {e}")

# Example usage
asset = "EURUSD"  # Replace with your desired asset
direction = "call"  # Or "put"
amount = 10  # Adjust the amount as needed
expiry_time = 5  # Adjust the expiry time in minutes

# Place a trade
place_trade(asset, direction, amount, expiry_time)

# Check balance
check_balance()

# Get trade history
get_trade_history()

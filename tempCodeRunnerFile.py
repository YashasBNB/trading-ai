from iqoptionapi.stable_api import IQ_Option
import logging

# Replace with your IQ Option credentials
email = "yashasnaidu3@gmail.com"
password = "King@2005"

# Connect to IQ Option
Iq = IQ_Option(email, password)
Iq.connect()

if Iq.check_connect():
    print("Successfully connected to IQ Option")
    
    # Get available assets
    assets = Iq.get_all_open_time()
    
    # Print the entire assets structure to understand its format
    print("Available Assets:")
    print(assets)  # Add this line to inspect the data structure
    
    # Assuming assets['binary'] is the right place to look for binary options
    if 'binary' in assets:
        for asset in assets['binary']:
            print(f"Asset: {asset['name']}, Available: {asset['open']}")
    else:
        print("No binary options available.")
else:
    print("Failed to connect to IQ Option")

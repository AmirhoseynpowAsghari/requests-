import requests

def get_btc_price():
    # CoinGecko API endpoint for cryptocurrency prices
    api_endpoint = "https://api.coingecko.com/api/v3/simple/price"

    # Parameters for the request
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }

    try:
        # Make the request to the API
        response = requests.get(api_endpoint, params=params)
        data = response.json()

        # Extract the BTC price from the response
        btc_price = data['bitcoin']['usd']

        return btc_price

    except Exception as e:
        print(f"Error: {e}")
        return None

# Get and print the current price of BTC
btc_price = get_btc_price()

if btc_price is not None:
    print(f"Current BTC Price: ${btc_price}")
else:
    print("Failed to retrieve BTC price.")

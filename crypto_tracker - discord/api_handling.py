import requests


# import configparser
# config = configparser.ConfigParser()
# config.read('config/config.ini')

# ❗Use if you want to add something related to the operation of the API


def get_crypto_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    # headers = {'x-cg-pro-api-key': api_key}
    response = requests.get(url)
    data = response.json()
    return data[coin]['usd']

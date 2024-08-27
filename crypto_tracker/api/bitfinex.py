import requests


def get_price(coin):
    url = f"https://api.bitfinex.com/v1/pubticker/{coin}usd"
    response = requests.get(url)
    data = response.json()
    return float(data['last_price'])

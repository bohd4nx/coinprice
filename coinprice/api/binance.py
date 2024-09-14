import requests


def get_price(coin):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

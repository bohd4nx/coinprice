import requests


def get_price(coin):
    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={coin.upper()}-USDT"
    response = requests.get(url)
    data = response.json()
    return float(data['data']['price'])

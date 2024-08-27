import requests


def get_price(coin):
    url = f"https://api.bybit.com/v2/public/tickers?symbol={coin.upper()}USD"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return float(data['result'][0]['last_price'])

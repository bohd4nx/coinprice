import requests


def get_price(symbol):
    api = 'https://www.okx.com/api/v5/market/ticker?instId={symbol}-USDT'
    url = api.format(symbol=symbol.upper())
    response = requests.get(url)
    data = response.json()
    return float(data['data'][0]['last'])

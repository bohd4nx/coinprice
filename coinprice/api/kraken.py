import requests


def get_price(coin):
    url = f"https://api.kraken.com/0/public/Ticker?pair={coin.upper()}USD"
    response = requests.get(url)
    data = response.json()
    return float(data['result'][list(data['result'].keys())[0]]['c'][0])

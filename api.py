import requests

def Binance(coin):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def Bybit(coin):
    url = f"https://api.bybit.com/v2/public/tickers?symbol={coin.upper()}USD"
    response = requests.get(url)
    data = response.json()
    return float(data['result'][0]['last_price'])


# def OKX(coin):
#     url = f"https://www.okex.com/api/market/v3/ticker/price?instId={coin.upper()}-USDT"
#     response = requests.get(url)
#     data = response.json()
#     return float(data['data'][0]['last'])

def Coinbase(coin):
    url = f"https://api.coinbase.com/v2/prices/{coin.upper()}-USD/spot"
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])

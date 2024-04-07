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


def Bitfinex(coin):
    url = f"https://api.bitfinex.com/v1/pubticker/{coin}usd"
    response = requests.get(url)
    data = response.json()
    return float(data['last_price'])


def Coinbase(coin):
    url = f"https://api.coinbase.com/v2/prices/{coin.upper()}-USD/spot"
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])


# def CoinGecko(coin):
#     url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
#     response = requests.get(url)
#     data = response.json()
#     return data[coin]['usd']


# def TradingView(coin):
#     url = f"https://api.tradingview.com/crypto/quotesUSD?symbols={coin}"
#     response = requests.get(url)
#     data = response.json()
#     return data[0]['price']

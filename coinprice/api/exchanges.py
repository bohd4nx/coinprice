import requests


def get_price(exchange, coin):
    """Fetch the current price of a cryptocurrency from various exchanges.

    Args:
        exchange (str): The name of the exchange (e.g., 'binance').
        coin (str): The symbol of the cryptocurrency (e.g., 'BTC').

    Returns:
        float: The price of the cryptocurrency in USDT.

    Raises:
        ValueError: If the response does not contain a valid price or the exchange is unsupported.
    """
    urls = {
        "binance": f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT",
        "bitfinex": f"https://api.bitfinex.com/v1/pubticker/{coin.lower()}usd",
        "coinbase": f"https://api.coinbase.com/v2/prices/{coin.upper()}-USD/spot",
        "gateio": f"https://api.gate.io/api2/1/ticker/{coin.lower()}_usdt",
        "huobi": f"https://api.huobi.pro/market/detail/merged?symbol={coin.lower()}usdt",
        "kraken": f"https://api.kraken.com/0/public/Ticker?pair={coin.upper()}USD",
        "kucoin": f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={coin.upper()}-USDT",
        "okx": f"https://www.okx.com/api/v5/market/ticker?instId={coin.upper()}-USDT",
        # "bybit": f"https://api.bybit.com/v2/public/tickers?symbol={coin.upper()}USDT" # Isn't working
    }

    if exchange.lower() not in urls:
        raise ValueError(f"Exchange '{exchange}' is not supported.")

    url = urls[exchange.lower()]
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Parse price based on exchange
        if exchange.lower() == "binance":
            return float(data['price'])
        elif exchange.lower() == "bitfinex":
            return float(data['last_price'])
        elif exchange.lower() == "coinbase":
            return float(data['data']['amount'])
        elif exchange.lower() == "gateio":
            return float(data['last'])
        elif exchange.lower() == "huobi":
            return float(data['tick']['close'])
        elif exchange.lower() == "kraken":
            return float(data['result'][list(data['result'].keys())[0]]['c'][0])
        elif exchange.lower() == "kucoin":
            return float(data['data']['price'])
        elif exchange.lower() == "okx":
            return float(data['data'][0]['last'])
        # elif exchange.lower() == "bybit":
        #     return float(data['result'][0]['last_price'])

    except (requests.RequestException, KeyError, ValueError) as e:
        raise ValueError(f"Failed to fetch price for {coin} on {exchange}: {e}") from e

from functools import reduce
from operator import getitem

import requests


def get_nested_value(data, path):
    """
    Get nested dictionary value using a path list.
    
    Args:
        data (dict): The dictionary to traverse
        path (list|str): List of keys or single key to access nested value
        
    Returns:
        Any: The value found at the specified path
        
    Raises:
        KeyError: If path is invalid
    """
    return reduce(getitem, path if isinstance(path, list) else [path], data)


def get_price(exchange, coin):
    """
    Fetch cryptocurrency price from specified exchange.
    
    Args:
        exchange (str): Exchange name (e.g. 'binance', 'coinbase')
        coin (str): Cryptocurrency symbol (e.g. 'btc', 'eth')
        
    Returns:
        float: Current price in USD/USDT
        
    Raises:
        ValueError: If exchange is unsupported or API call fails
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
        "bybit": f"https://api.bybit.com/v5/market/tickers?category=inverse&symbol={coin.upper()}USDT",
        "mexc": f"https://api.mexc.com/api/v3/ticker/price?symbol={coin.upper()}USDT",
        "whitebit": f"https://whitebit.com/api/v1/public/ticker?market={coin.upper()}_USDT"
    }

    if exchange.lower() not in urls:
        raise ValueError(f"Exchange '{exchange}' is not supported.")

    url = urls[exchange.lower()]

    price_parsers = {
        "binance": ["price"],
        "bitfinex": ["last_price"],
        "coinbase": ["data", "amount"],
        "gateio": ["last"],
        "huobi": ["tick", "close"],
        "kraken": lambda d: d["result"][list(d["result"].keys())[0]]["c"][0],
        "kucoin": ["data", "price"],
        "okx": ["data", 0, "last"],
        "whitebit": ["result", "last"],
        "mexc": ["price"],
        "bybit": ["result", "list", 0, "lastPrice"]
    }

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        parser = price_parsers.get(exchange.lower())
        if parser is None:
            raise ValueError(f"No parser defined for exchange {exchange}")

        if callable(parser):
            price = parser(data)
        else:
            price = get_nested_value(data, parser)

        return float(price)

    except (requests.RequestException, KeyError, ValueError) as e:
        raise ValueError(f"Failed to fetch price for {coin} on {exchange}: {e}") from e

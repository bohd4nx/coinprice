import time
from colorama import Fore, Style
from crypto_tracker.api import binance, bybit, coinbase, bitfinex, coingecko
from crypto_tracker.utils import print_price, print_divider


def track_prices(args):
    coin = args.coin.lower()
    interval = args.interval
    previous_prices = {}

    exchanges = {
        'binance': binance.get_price,
        # 'coingecko': coingecko.get_price,
        'coinbase': coinbase.get_price,
        'bitfinex': bitfinex.get_price
        # 'bybit': bybit.get_price,
    }

    try:
        for exchange in exchanges.keys():
            if getattr(args, exchange):
                track_exchange(exchange, exchanges[exchange], coin, interval, previous_prices)

        if not any([args.binance, args.coinbase, args.bitfinex]):
            track_all_exchanges(exchanges, coin, interval, previous_prices)

    except KeyboardInterrupt:
        print("Exiting...")


def track_exchange(exchange, get_price_func, coin, interval, previous_prices):
    while True:
        try:
            price = get_price_func(coin)
            print_price(exchange.capitalize(), price, coin, previous_prices)
            previous_prices[exchange.capitalize()] = price
        except Exception:
            print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {exchange.capitalize()} is {Fore.RED}not available{Style.RESET_ALL}")
        time.sleep(interval)


def track_all_exchanges(exchanges, coin, interval, previous_prices):
    print(f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}all available exchanges{Style.RESET_ALL} with an interval of {interval} seconds.\n")

    while True:
        for exchange, get_price_func in exchanges.items():
            try:
                price = get_price_func(coin)
                print_price(exchange.capitalize(), price, coin, previous_prices)
                previous_prices[exchange.capitalize()] = price
            except Exception:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {exchange.capitalize()} is {Fore.RED}N/A{Style.RESET_ALL}")

        print_divider()
        time.sleep(interval)

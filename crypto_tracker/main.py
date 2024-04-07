import argparse
import time
from colorama import Fore, Style
from crypto_tracker.api import *


def main():
    parser = argparse.ArgumentParser(
        epilog=f'examples: \n'
               f'  price btc                        Track the price of Bitcoin from all exchanges.\n'
               f'  price eth --binance              Track the price of Bitcoin from Binance.\n'
               f'  price ltc --bybit --interval 10  Track the price of Litecoin from Bybit with a check interval of 10 seconds.\n'
               '\n'
               f'{Fore.GREEN}This is an open-source project. Visit{Style.RESET_ALL} {Fore.CYAN}https://github.com/7GitGuru/crypto-tracker{Style.RESET_ALL} {Fore.GREEN}for more information.{Style.RESET_ALL}\n'
               '\n'
               f'{Fore.GREEN}List of cryptocurrencies:{Style.RESET_ALL} {Fore.CYAN}https://github.com/7GitGuru/crypto-tracker/blob/main/coin-names.json{Style.RESET_ALL}\n'
               '\n'
               f'{Fore.GREEN}Support the developer by donating:{Style.RESET_ALL} {Fore.CYAN}https://www.buymeacoffee.com/bohd4n{Style.RESET_ALL}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('coin', type=str, help='The cryptocurrency to track.')
    parser.add_argument('--interval', type=int, default=15,
                        help='Interval in seconds to check the price (default: 15).')
    parser.add_argument('--binance', action='store_true', help='Track from Binance.')
    parser.add_argument('--bybit', action='store_true', help='Track from Bybit.')
    parser.add_argument('--coinbase', action='store_true', help='Track from Coinbase.')
    parser.add_argument('--bitfinex', action='store_true', help='Track from Bitfinex.')
    args = parser.parse_args()

    coin = args.coin.lower()
    interval = args.interval

    try:
        previous_prices = {}

        def print_price(exchange, price):
            if exchange in previous_prices:
                previous_price = previous_prices[exchange]
                if price < previous_price:
                    color = Fore.RED
                elif price > previous_price:
                    color = Fore.GREEN
                else:
                    color = Fore.WHITE
            else:
                color = Fore.WHITE
            print(
                f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {exchange} is {color}${price}{Style.RESET_ALL}")
            # print("\n")

        def print_divider():
            print(f"{Fore.MAGENTA}{'-' * 50}{Style.RESET_ALL}")

        for exchange in ['binance', 'bybit', 'coinbase', 'bitfinex']:
            # print(f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}{exchange}{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL}\n")
            if getattr(args, exchange):
                while True:
                    try:
                        price = globals()[exchange.capitalize()](coin)
                        print_price(exchange.capitalize(), price)
                        previous_prices[exchange.capitalize()] = price
                    except Exception:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {exchange.capitalize()} is {Fore.RED}not available{Style.RESET_ALL}")
                        # print("\n")
                    time.sleep(interval)

        if not any([args.binance, args.bybit, args.coinbase, args.bitfinex]):
            print(f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}all available exchanges{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL}\n")
            print_divider()
            while True:
                try:
                    price = Binance(coin)
                    print_price("Binance", price)
                    previous_prices["Binance"] = price
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Binance is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    price = Bybit(coin)
                    print_price("Bybit", price)
                    previous_prices["Bybit"] = price
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bybit is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    price = Coinbase(coin)
                    print_price("Coinbase", price)
                    previous_prices["Coinbase"] = price
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Coinbase is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    price = Bitfinex(coin)
                    print_price("Bitfinex", price)
                    previous_prices["Bitfinex"] = price
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bitfinex is {Fore.RED}not available{Style.RESET_ALL}")
                print_divider()
                time.sleep(interval)

    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()

import argparse
import time
from colorama import Fore, Style
from crypto_tracker.api import *
# import random


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
    # parser.add_argument('--coingecko', action='store_true', help='Track from CoinGecko.')
    # parser.add_argument('--tradingview', action='store_true', help='Track from TradingView.')
    args = parser.parse_args()

    coin = args.coin.lower()
    interval = args.interval

    try:
        if args.binance:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Binance{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Binance is {Fore.LIGHTGREEN_EX}${Binance(coin)}{Style.RESET_ALL}\n")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Binance is {Fore.RED}not available{Style.RESET_ALL}\n")
                time.sleep(interval)

        if args.bybit:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bybit{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bybit is {Fore.LIGHTGREEN_EX}${Bybit(coin)}{Style.RESET_ALL}\n")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bybit{Style.RESET_ALL} is {Fore.RED}not available{Style.RESET_ALL}\n")
                time.sleep(interval)

        if args.coinbase:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Coinbase{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Coinbase is {Fore.LIGHTGREEN_EX}${Coinbase(coin)}{Style.RESET_ALL}\n")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Coinbase is {Fore.RED}not available{Style.RESET_ALL}\n")
                time.sleep(interval)

        if args.bitfinex:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bitfinex{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bitfinex is {Fore.LIGHTGREEN_EX}${Binance(coin)}{Style.RESET_ALL}\n")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bitfinex is {Fore.RED}not available{Style.RESET_ALL}\n")
                time.sleep(interval)

        if not any([args.binance, args.bybit, args.coinbase, args.bitfinex]):  ## + args.coingecko | args.tradingview
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}all available exchanges{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Binance is {Fore.LIGHTGREEN_EX}${Binance(coin)}{Style.RESET_ALL}")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Binance is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bybit is {Fore.LIGHTGREEN_EX}${Bybit(coin)}{Style.RESET_ALL}")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bybit is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Coinbase is {Fore.LIGHTGREEN_EX}${Coinbase(coin)}{Style.RESET_ALL}")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Coinbase is {Fore.RED}not available{Style.RESET_ALL}")
                try:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bitfinex is {Fore.LIGHTGREEN_EX}${Bitfinex(coin)}{Style.RESET_ALL}\n")
                except Exception:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on Bitfinex is {Fore.RED}not available{Style.RESET_ALL}\n")
                time.sleep(interval)

    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()

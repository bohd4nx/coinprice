import argparse
import time
from colorama import Fore, Style
from crypto_tracker.api import *


def main():
    parser = argparse.ArgumentParser(
        epilog=f'{Fore.CYAN}Exchanges:{Style.RESET_ALL}\n'
               f'  {Fore.YELLOW}--binance{Style.RESET_ALL}     Track from Binance.\n'
               f'  {Fore.YELLOW}--bybit{Style.RESET_ALL}       Track from Bybit.\n'
               f'  {Fore.YELLOW}--coinbase{Style.RESET_ALL}    Track from Coinbase.\n'
               '\n'
               f'{Fore.CYAN}Examples:{Style.RESET_ALL}\n'
               f'  {Fore.YELLOW}price btc{Style.RESET_ALL}                       Track the price of Bitcoin from all exchanges.\n'
               f'  {Fore.YELLOW}price eth --binance{Style.RESET_ALL}             Track the price of Bitcoin from Binance.\n'
               f'  {Fore.YELLOW}price ltc --bybit --interval 10{Style.RESET_ALL} Track the price of Ethereum from Bybit with a check interval of 10 seconds.\n'
               '\n'
               f'{Fore.GREEN}This is an open-source project. Visit https://github.com/7GitGuru/crypto-tracker for more information.{Style.RESET_ALL}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('coin', type=str, help='The cryptocurrency to track.')
    parser.add_argument('--interval', type=int, default=15,
                        help='Interval in seconds to check the price (default: 15).')
    parser.add_argument('--binance', action='store_true', help='Track from Binance.')
    parser.add_argument('--bybit', action='store_true', help='Track from Bybit.')
    parser.add_argument('--coinbase', action='store_true', help='Track from Coinbase.')
    args = parser.parse_args()

    coin = args.coin.lower()
    interval = args.interval

    if args.binance:
        print(f"{Fore.GREEN}{coin.upper()} price on Binance is ${Binance(coin)}{Style.RESET_ALL}")
    if args.bybit:
        print(f"{Fore.GREEN}{coin.upper()} price on Bybit is ${Bybit(coin)}{Style.RESET_ALL}")
    if args.coinbase:
        print(f"{Fore.GREEN}{coin.upper()} price on Coinbase is ${Coinbase(coin)}{Style.RESET_ALL}")

    if not any([args.binance, args.bybit, args.coinbase]):
        print(
            f"Tracking {coin.upper()} price from all available exchanges with an interval of {interval} seconds. Press Ctrl+C to exit.")

        try:
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.YELLOW}Binance{Style.RESET_ALL} is {Fore.GREEN}${Binance(coin)}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bybit{Style.RESET_ALL} is {Fore.GREEN}${Bybit(coin)}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.BLUE}Coinbase{Style.RESET_ALL} is {Fore.GREEN}${Coinbase(coin)}{Style.RESET_ALL}")
                print()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Exiting...")


if __name__ == "__main__":
    main()

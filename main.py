import argparse
import time
import random
from colorama import Fore, Style
from crypto_tracker.api import *


def main():
    parser = argparse.ArgumentParser(
        epilog=f'{Fore.CYAN}💲Exchanges:{Style.RESET_ALL}\n'
               f'  {Fore.YELLOW}--binance{Style.RESET_ALL}     Track from Binance.\n'
               f'  {Fore.YELLOW}--bybit{Style.RESET_ALL}       Track from Bybit.\n'
               f'  {Fore.YELLOW}--coinbase{Style.RESET_ALL}    Track from Coinbase.\n'
               '\n'
               f'{Fore.CYAN}⚙️Examples:{Style.RESET_ALL}\n'
               f'  {Fore.YELLOW}price btc{Style.RESET_ALL}                       Track the price of Bitcoin from all exchanges.\n'
               f'  {Fore.YELLOW}price eth --binance{Style.RESET_ALL}             Track the price of Bitcoin from Binance.\n'
               f'  {Fore.YELLOW}price ltc --bybit --interval 10{Style.RESET_ALL} Track the price of Ethereum from Bybit with a check interval of 10 seconds.\n'
               '\n'
               f'{Fore.GREEN}🛠️This is an open-source project. Visit{Style.RESET_ALL} {Fore.CYAN}https://github.com/7GitGuru/crypto-tracker{Style.RESET_ALL} {Fore.GREEN}for more information.{Style.RESET_ALL}\n'
               '\n'
               f'{Fore.GREEN}❤️Support the developer by donating:{Style.RESET_ALL} {Fore.CYAN}https://www.buymeacoffee.com/bohd4n{Style.RESET_ALL}',
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

    try:
        if args.binance:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Binance{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.YELLOW}Binance{Style.RESET_ALL} is {Fore.GREEN}${Binance(coin)}{Style.RESET_ALL}\n")
                if random.random() < 0.2:
                    print("❤️Support the developer by donating: https://www.buymeacoffee.com/bohd4n\n")
                time.sleep(interval)

        if args.bybit:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bybit{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bybit{Style.RESET_ALL} is {Fore.GREEN}${Bybit(coin)}{Style.RESET_ALL}\n")
                if random.random() < 0.2:
                    print("❤️Support the developer by donating: https://www.buymeacoffee.com/bohd4n\n")
                time.sleep(interval)

        if args.coinbase:
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Coinbase{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.BLUE}Coinbase{Style.RESET_ALL} is {Fore.GREEN}${Coinbase(coin)}{Style.RESET_ALL}\n")
                if random.random() < 0.2:
                    print("❤️Support the developer by donating: https://www.buymeacoffee.com/bohd4n\n")
                time.sleep(interval)

        if not any([args.binance, args.bybit, args.coinbase]):
            print(
                f"Tracking {Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}all available exchanges{Style.RESET_ALL} with an interval of {Fore.RED}{interval} seconds.{Style.RESET_ALL} Press Ctrl+C to exit.\n")
            while True:
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.YELLOW}Binance{Style.RESET_ALL} is {Fore.GREEN}${Binance(coin)}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.CYAN}Bybit{Style.RESET_ALL} is {Fore.GREEN}${Bybit(coin)}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {Fore.BLUE}Coinbase{Style.RESET_ALL} is {Fore.GREEN}${Coinbase(coin)}{Style.RESET_ALL}\n")
                if random.random() < 0.2:
                    print("❤️Support the developer by donating: https://www.buymeacoffee.com/bohd4n\n")
                time.sleep(interval)

    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()

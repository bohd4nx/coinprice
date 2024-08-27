import argparse
from colorama import Fore, Style


def parse_arguments():
    parser = argparse.ArgumentParser(
        epilog=f'examples: \n'
               f'  price btc                        Track the price of Bitcoin from all exchanges.\n'
               f'  price eth --binance              Track the price of Ethereums from Binance.\n'
               f'  price ltc --coinbase --interval 10  Track the price of Litecoin from Coinbase with a check interval of 10 seconds.\n'
               '\n'
               f'{Fore.GREEN}This is an open-source project. Visit{Style.RESET_ALL} {Fore.CYAN}https://github.com/bohd4nx/crypto-tracker{Style.RESET_ALL} {Fore.GREEN}for more information.{Style.RESET_ALL}\n'
               '\n'
               f'{Fore.GREEN}Support the developer by donating:{Style.RESET_ALL} {Fore.CYAN}https://www.buymeacoffee.com/bohd4n{Style.RESET_ALL}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('coin', type=str, help='The cryptocurrency to track.')
    parser.add_argument('--interval', type=int, default=15,
                        help='Interval in seconds to check the price (default: 15).')
    parser.add_argument('--binance', action='store_true', help='Track from Binance.')
    # parser.add_argument('--bybit', action='store_true', help='Track from Bybit.')
    parser.add_argument('--coinbase', action='store_true', help='Track from Coinbase.')
    parser.add_argument('--bitfinex', action='store_true', help='Track from Bitfinex.')
    # parser.add_argument('--coingecko', action='store_true', help='Track from CoinGecko.')

    return parser.parse_args()

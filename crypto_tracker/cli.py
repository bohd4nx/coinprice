import argparse
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        pass

    def add_argument(self, action):
        pass

    def start_section(self, heading):
        if heading in ['examples', '']:
            super().start_section(heading)

    def end_section(self):
        if self._current_section and self._current_section.heading in ['examples', '']:
            super().end_section()


def parse_arguments():
    parser = argparse.ArgumentParser(
        formatter_class=CustomHelpFormatter,
        description=f"{Fore.GREEN}Crypto Tracker{Style.RESET_ALL} is a Python module that allows you to track the prices of cryptocurrencies in real-time. "
                    "You can specify the cryptocurrency you want to track and the module will provide you with live updates on its price.",
        epilog=f'{Fore.YELLOW}Examples:{Style.RESET_ALL} \n'
               f'   {Fore.CYAN}price btc{Style.RESET_ALL}                        Track Bitcoin price from all available exchanges.\n'
               f'   {Fore.CYAN}price eth --binance{Style.RESET_ALL}              Track Ethereum price from Binance with default interval.\n'
               f'   {Fore.CYAN}price ltc --coinbase -t 10{Style.RESET_ALL}       Track Litecoin price on Coinbase in 10 second intervals.\n'
               f'   {Fore.CYAN}price 8num{Style.RESET_ALL}                       Track Anonymous Telegram Numbers price.\n'
               '\n'
               f'{Fore.GREEN}This is an open-source project. Visit{Style.RESET_ALL} {Fore.CYAN}https://github.com/bohd4nx/crypto-tracker{Style.RESET_ALL}\n'
               f'{Fore.GREEN}Support the developer by donating:{Style.RESET_ALL} {Fore.CYAN}https://www.buymeacoffee.com/bohd4n{Style.RESET_ALL}\n'
    )
    parser.add_argument('coin', type=str, help='The cryptocurrency to track or "8num" for anonymous number prices.')
    parser.add_argument('-t', '--interval', type=int, default=30,
                        help='Interval in seconds to check the price (default: 30).')
    parser.add_argument('--binance', action='store_true', help='Track from Binance.')
    parser.add_argument('--coinbase', action='store_true', help='Track from Coinbase.')
    parser.add_argument('--bitfinex', action='store_true', help='Track from Bitfinex.')
    parser.add_argument('--kucoin', action='store_true', help='Track from KuCoin.')
    parser.add_argument('--gateio', action='store_true', help='Track from Gate.io.')
    parser.add_argument('--kraken', action='store_true', help='Track from Kraken.')
    parser.add_argument('--huobi', action='store_true', help='Track from Huobi (HTX).')
    parser.add_argument('--okx', action='store_true', help='Track from OKX.')

    return parser.parse_args()

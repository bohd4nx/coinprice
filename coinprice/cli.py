import argparse

from colorama import Fore, Style, init

from coinprice.app import check_interval

init(autoreset=True)


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        """Skip usage section in help message."""
        pass

    def add_argument(self, action):
        """Skip arguments section in help message."""
        pass

    def start_section(self, heading):
        """Include only specific sections in the help message."""
        if heading in ['examples', '']:
            super().start_section(heading)

    def end_section(self):
        """End only allowed sections in the help message."""
        if self._current_section and self._current_section.heading in ['examples', '']:
            super().end_section()


def parse_arguments():
    parser = argparse.ArgumentParser(
        formatter_class=CustomHelpFormatter,
        description=(
            f"{Style.BRIGHT}{Fore.GREEN}Coinprice{Style.RESET_ALL} is a Python module that allows you to track "
            f"the prices of cryptocurrencies in real-time. You can specify the cryptocurrency you want to track "
            f"and the module will provide you with live updates on its price."
        ),
        epilog=(
            f"{Fore.YELLOW}Examples:{Style.RESET_ALL}\n"
            f"   {Fore.CYAN}price btc{Style.RESET_ALL}                        Track Bitcoin price from all available exchanges.\n"
            f"   {Fore.CYAN}price eth --binance{Style.RESET_ALL}              Track Ethereum price from Binance with default interval.\n"
            f"   {Fore.CYAN}price ltc --coinbase -t 10{Style.RESET_ALL}       Track Litecoin price on Coinbase in 10 second intervals.\n"
            f"   {Fore.CYAN}price 8num{Style.RESET_ALL}                       Track Anonymous Telegram Numbers price from fragment.com\n\n"
            f"{Fore.GREEN}This is an open-source project. Visit{Style.RESET_ALL} {Fore.CYAN}https://github.com/bohd4nx/coinprice{Style.RESET_ALL}\n"
        )
    )

    parser.add_argument(
        'coin', type=str,
        help='The cryptocurrency to track or "8num" for anonymous number prices.'
    )

    parser.add_argument(
        '-t', '--interval', type=check_interval, default=30,
        help='Interval in seconds to check the price (default: 30).'
    )

    exchanges = [
        ('--binance', 'Track from Binance.'),
        ('--coinbase', 'Track from Coinbase.'),
        ('--bitfinex', 'Track from Bitfinex.'),
        ('--kucoin', 'Track from KuCoin.'),
        ('--gateio', 'Track from Gate.io.'),
        ('--kraken', 'Track from Kraken.'),
        ('--huobi', 'Track from Huobi (HTX).'),
        ('--okx', 'Track from OKX.')
    ]

    for arg, help_text in exchanges:
        parser.add_argument(arg, action='store_true', help=help_text)

    return parser.parse_args()

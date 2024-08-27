from colorama import Fore, Style


def print_price(exchange, price, coin, previous_prices):
    if exchange in previous_prices:
        previous_price = previous_prices[exchange]
        color = get_color(price, previous_price)
    else:
        color = Fore.WHITE

    print(f"{Fore.LIGHTYELLOW_EX}{coin.upper()}{Style.RESET_ALL} price on {exchange} is {color}${price}{Style.RESET_ALL}")


def get_color(price, previous_price):
    if price < previous_price:
        return Fore.RED
    elif price > previous_price:
        return Fore.GREEN
    else:
        return Fore.WHITE


def print_divider():
    print(f"{Fore.MAGENTA}{'-' * 50}{Style.RESET_ALL}")

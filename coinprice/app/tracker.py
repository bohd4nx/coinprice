import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from rich.console import Console
from rich.table import Table

from coinprice.api import binance, coinbase, bitfinex, kucoin, gateio, kraken, huobi, okx
from coinprice.app import clear_console, terminal_title

console = Console()


def fetch_price(exchange, get_price_func, coin):
    try:
        price = get_price_func(coin)
        return exchange, price, None
    except Exception as e:
        return exchange, None, str(e)


def format_price(price):
    """Format the price based on its value."""
    if price < 0.1:
        return f"{price:.6f}"
    else:
        return f"{price:,.2f}"


def track_prices(args):
    coin = args.coin.lower()
    interval = args.interval
    previous_prices = {}

    terminal_title(coin.upper())

    # All available exchanges
    all_exchanges = {
        'Coinbase': coinbase.get_price,
        'Bitfinex': bitfinex.get_price,
        'Gate.io': gateio.get_price,
        'Kraken': kraken.get_price,
        'Binance': binance.get_price,
        'KuCoin': kucoin.get_price,
        'Huobi': huobi.get_price,
        'OKX': okx.get_price
    }

    # Filter exchanges
    exchanges = {name: func for name, func in all_exchanges.items() if getattr(args, name.lower(), False)}

    # Use all available exchanges if none are selected
    if not exchanges:
        exchanges = all_exchanges

    try:
        while True:
            with ThreadPoolExecutor(max_workers=len(exchanges)) as executor:
                futures = {executor.submit(fetch_price, exchange, get_price_func, coin): exchange for
                           exchange, get_price_func in exchanges.items()}
                results = [future.result() for future in futures]
            valid_results = [(exchange, price) for exchange, price, error in results if price is not None]
            sorted_results = sorted(valid_results, key=lambda x: x[1], reverse=True)

            table = Table(show_header=True, header_style="bold blue_violet",
                          title="Made by [bold link=https://bohd4n.dev/]@bohd4nx[/bold link]\n",
                          title_justify="center")
            table.add_column("Exchange", style="bold bright_cyan")
            table.add_column(f"[bold orange3]{coin.upper()}[/bold orange3] Price", justify="center")
            table.add_column("Changes", justify="center")

            for exchange, price in sorted_results:
                formatted_price = format_price(price)
                change = get_change(previous_prices, exchange, price)
                table.add_row(exchange, f"${formatted_price}", change)
                previous_prices[exchange] = price

            if not table.row_count:
                table.add_row("N/A", "N/A", "N/A")

            clear_console()
            console.print(table)
            last_updated_time = datetime.now().strftime('%H:%M:%S')

            # Display the initial Last Updated line
            countdown = interval
            while countdown > 0:
                console.print(f"  Last Updated at {last_updated_time} | {countdown}s", end="\r")
                time.sleep(1)
                countdown -= 1

            # Print new line after countdown finishes
            console.print(f"  Last Updated at {last_updated_time} | ...")

    except KeyboardInterrupt:
        console.print("\n\n" + " " * 13 + "[bold red3]Exiting...[/bold red3]")


def get_change(previous_prices, exchange, price):
    if exchange in previous_prices:
        previous_price = previous_prices[exchange]
        if price < previous_price:
            return f"[red3]- ${previous_price - price:.2f}[/red3]"
        elif price > previous_price:
            return f"[green1]+ ${price - previous_price:.2f}[/green1]"
    return ""
    # return "± $0.00"

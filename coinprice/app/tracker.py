import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from rich.console import Console
from rich.table import Table

from coinprice.api import get_price
from coinprice.app.utils import clear_console, terminal_title

console = Console()


def fetch_price(exchange, coin):
    """
    Fetch price from single exchange safely.
    
    Args:
        exchange (str): Exchange name
        coin (str): Coin symbol
        
    Returns:
        tuple: (exchange, price, error) where:
            - price is float or None if error
            - error is str or None if success
    """
    try:
        price = get_price(exchange, coin)
        return exchange, price, None
    except Exception as e:
        return exchange, None, str(e)


def format_price(price):
    """
    Format price value with appropriate decimal places.
    
    Args:
        price (float): Price value to format
        
    Returns:
        str: Formatted price string
    """
    if price < 0.1:
        return f"{price:.6f}"
    else:
        return f"{price:,.2f}"


def track_prices(args):
    """
    Track cryptocurrency prices across multiple exchanges.
    
    Args:
        args (Namespace): Arguments containing:
            - coin (str): Coin to track
            - interval (int): Update interval in seconds
            - exchange flags (bool): Which exchanges to include
            
    KeyboardInterrupt can be used to stop tracking
    """
    coin = args.coin.lower()
    interval = args.interval
    previous_prices = {}

    terminal_title(coin.upper())

    all_exchanges = [
        "Binance", "Coinbase", "Bitfinex", "Gate.io", "Kraken",
        "KuCoin", "Huobi", "OKX", "Bybit", "MEXC", "WhiteBIT",
    ]

    exchanges = [exchange for exchange in all_exchanges if getattr(args, exchange.lower(), False)]

    if not exchanges:
        exchanges = all_exchanges

    try:
        while True:
            with ThreadPoolExecutor(max_workers=len(exchanges)) as executor:
                futures = {executor.submit(fetch_price, exchange, coin): exchange for exchange in exchanges}
                results = [future.result() for future in futures]
            valid_results = [(exchange, price) for exchange, price, error in results if price is not None]
            sorted_results = sorted(valid_results, key=lambda x: x[1], reverse=True)

            table = Table(show_header=True, header_style="bold blue_violet",
                          title="Made by [bold link=https://bohd4n.dev/]@bohd4nx[/bold link]\n",
                          title_justify="center")
            table.add_column("Exchange", style="bold bright_cyan")
            table.add_column(f"[bold orange3]${coin.upper()}[/bold orange3] Price", justify="center")
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

            countdown = interval
            while countdown > 0:
                console.print(f"  Last Updated at {last_updated_time} | {countdown}s", end="\r")
                time.sleep(1)
                countdown -= 1

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

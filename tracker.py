import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.table import Table

from coinprice.api import binance, coinbase, bitfinex, kucoin, gateio, kraken, huobi, okx
from coinprice.utils import clear_console

console = Console()


def fetch_price(exchange, get_price_func, coin):
    try:
        price = get_price_func(coin)
        return exchange, price, None
    except Exception as e:
        return exchange, None, str(e)


def track_prices(args):
    coin = args.coin.lower()
    interval = args.interval
    previous_prices = {}

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
                futures = {executor.submit(fetch_price, exchange, get_price_func, coin): exchange for exchange, get_price_func in exchanges.items()}
                results = [future.result() for future in futures]
            valid_results = [(exchange, price) for exchange, price, error in results if price is not None]
            sorted_results = sorted(valid_results, key=lambda x: x[1], reverse=True)

            table = Table(show_header=True, header_style="bold blue_violet",
                          title="[gold3]Made by [link=https://github.com/bohd4nx]@bohd4nx[/link][/gold3]\n\n"
                                "[turquoise2][link=https://github.com/bohd4nx/crypto-tracker]Github[/link] | [link=https://buymeacoffee.com/bohd4n]Donate[/link] "
                                "| [link=https://coinprice.bohd4n.dev/]Website[/link][/turquoise2]", title_justify="center")
            table.add_column("Exchange", style="bold bright_cyan")
            table.add_column(f"[orange3]{coin.upper()}[/orange3] Price", justify="center")
            table.add_column("Changes", justify="center")

            for exchange, price in sorted_results:
                change = get_change(previous_prices, exchange, price)
                table.add_row(exchange, f"${price:.2f}", change)
                previous_prices[exchange] = price

            if not table.row_count:
                table.add_row("N/A", "N/A", "N/A")

            clear_console()
            console.print(table)
            console.print(f"Last Updated: {datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
            time.sleep(interval)

    except KeyboardInterrupt:
        console.print("\n[bold red3]Exiting...[/bold red3] Made by [link=https://buymeacoffee.com/bohd4n]@bohd4nx[/link]")


def get_change(previous_prices, exchange, price):
    if exchange in previous_prices:
        previous_price = previous_prices[exchange]
        if price < previous_price:
            return f"[red3]- ${previous_price - price:.2f}[/red3]"
        elif price > previous_price:
            return f"[green1]+ ${price - previous_price:.2f}[/green1]"
    return "± $0.00"

import time
from datetime import datetime

from rich.console import Console
from rich.table import Table


from coinprice.api.fragment_api import get_price
from coinprice.utils import clear_console

console = Console()


def track_fragment_prices(interval):
    previous_price = None

    try:
        while True:
            current_price_ton, current_price_usd = get_price()

            if previous_price is not None:
                price_change = calculate_percentage(previous_price, current_price_ton)
            else:
                price_change = "± 0.00%"  # Initial value when there's no previous price
            previous_price = current_price_ton
            table = Table(show_header=True, header_style="bold blue_violet",
                          title="[gold3]Anonymous Numbers Price[/gold3]\n\n"
                                "[turquoise2][link=https://github.com/bohd4nx/crypto-tracker]Github[/link] | [link=https://buymeacoffee.com/bohd4n]Donate[/link] "
                                "| [link=https://coinprice.bohd4n.dev/]Website[/link][/turquoise2]", title_justify="center")
            table.add_column("[orange3]TON[/orange3] Price", justify="center")
            table.add_column("[orange3]USD[/orange3] Price", justify="center")
            table.add_column("[orange3][link=https://fragment.com/about#:~:text=collectibles%20are%20subject%20to%20a%205%25%20platform%20fee%20on%20each%20transaction.]Fee[/link][/orange3]", justify="center")
            table.add_column("Changes", justify="center")

            # Calculate -5% fee
            fee = current_price_ton * 0.05

            table.add_row(
                f"{current_price_ton:} TON",
                f"${current_price_usd:.2f}",
                f"{fee:.2f} TON",
                price_change
            )

            clear_console()
            console.print(table)
            console.print(f"Last Updated: {datetime.now().strftime('%d.%m.%y %H:%M:%S')}")

            time.sleep(interval)

    except KeyboardInterrupt:
        console.print("\n[bold red3]Exiting...[/bold red3] Made by [link=https://buymeacoffee.com/bohd4n]@bohd4nx[/link]")


def calculate_percentage(old_price, new_price):
    if old_price == 0:
        return "± 0.00%"

    percentage_change = ((new_price - old_price) / old_price) * 100

    if percentage_change < 0:
        return f"[red3]- {percentage_change:.2f}%[/red3]"
    elif percentage_change > 0:
        return f"[green1]+ {percentage_change:.2f}%[/green1]"
    else:
        return "± 0.00%"

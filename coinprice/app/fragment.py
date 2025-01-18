import time
from datetime import datetime

from rich.console import Console
from rich.table import Table

from coinprice.api import numprice
from coinprice.app.utils import clear_console, terminal_title

console = Console()


def track_numprice(interval):
    """
    Track and display Fragment Anonymous Numbers floor price in real-time.
    
    Creates an interactive table display showing:
    - Current floor price in TON
    - USD equivalent price
    - Platform fee (5%)
    - Price changes in percentage
    
    Args:
        interval (int): Update interval in seconds
        
    KeyboardInterrupt can be used to stop tracking
    """
    previous_price = 0
    coin = 'Anonymous Numbers'
    terminal_title(coin)

    try:
        while True:
            # Fetch current prices
            current_price_ton, current_price_usd = numprice()

            # Calculate price change percentage
            price_change = calculate_percentage(previous_price, current_price_ton)
            previous_price = current_price_ton

            # Create and configure display table
            table = Table(
                show_header=True,
                header_style="bold blue_violet",
                title="[bold gold3]Anonymous Numbers Price[/bold gold3]\n\n"
                      f"Made by [bold link=https://bohd4n.dev/]@bohd4nx[/bold link]",
                title_justify="center"
            )

            # Configure table columns
            table.add_column("[orange3]TON[/orange3] Price", justify="center")
            table.add_column("[orange3]USD[/orange3] Price", justify="center")
            table.add_column(
                "[orange3][link=https://fragment.com/about#:~:text=collectibles%20are%20subject%20to%20a%205%25%20platform%20fee%20on%20each%20transaction.]Fee[/link][/orange3]",
                justify="center"
            )
            table.add_column("Changes", justify="center")

            # Calculate platform fee (5%)
            fee = current_price_ton * 0.05

            # Add price data row
            table.add_row(
                f"{format(current_price_ton, ',.2f')} TON",
                f"${format(current_price_usd, ',.2f')}",
                f"{format(fee, ',.2f')} TON",
                price_change
            )

            # Display updated information
            clear_console()
            console.print(table)
            last_updated_time = datetime.now().strftime('%H:%M:%S')

            # Countdown timer between updates
            countdown = interval
            while countdown > 0:
                console.print(f"         Last Updated at {last_updated_time} | {countdown}s", end="\r")
                time.sleep(1)
                countdown -= 1

            console.print(f"         Last Updated at {last_updated_time} | ...")

    except KeyboardInterrupt:
        console.print("\n\n" + " " * 20 + "[bold red3]Exiting...[/bold red3]")


def calculate_percentage(old_price, new_price):
    """
    Calculate percentage change between old and new price.
    
    Args:
        old_price (float): Previous price value
        new_price (float): Current price value
        
    Returns:
        str: Formatted percentage string with color coding:
             - Red for price decrease
             - Green for price increase
             - Empty string for initial price
    """
    if old_price == 0:
        return ""

    percentage_change = ((new_price - old_price) / old_price) * 100

    if percentage_change < 0:
        return f"[red3]{percentage_change:.2f}%[/red3]"
    elif percentage_change > 0:
        return f"[green1]+ {percentage_change:.2f}%[/green1]"
    else:
        return "None"

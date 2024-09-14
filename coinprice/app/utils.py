import os


def clear_console():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def terminal_title(coin):
    if os.name == 'nt':  # Windows
        os.system(f'title {coin} Price ❘ @bohd4nx')
    else:  # Unix-like (Linux, macOS)
        os.system(f'printf "\\033]0;{coin} Price ❘ @bohd4nx\\007"')

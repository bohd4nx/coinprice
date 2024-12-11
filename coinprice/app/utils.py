import os
import random

from colorama import Fore, Style


def clear_console():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def terminal_title(coin):
    if os.name == 'nt':  # Windows
        os.system(f'title {coin} Price ❘ @bohd4nx')
    else:  # Unix-like (Linux, macOS)
        os.system(f'printf "\\033]0;{coin} Price\\007"')


def check_interval(value):
    int_value = int(value)
    if int_value < 5:
        phrases = [
            "Hold your horses! This isn't a Formula 1 race! The interval needs to be at least 5 seconds.",
            "Easy there! Crypto prices are not going to escape. Set at least 5 seconds.",
            "Chill out! We're not in a high-speed trading arena. Minimum interval is 5 seconds.",
            "Remember, Rome wasn't built in a day. Your crypto portfolio can wait 5 seconds.",
            "You’re not a day trader yet! Let’s keep the interval at 5 seconds, shall we?",
            "This isn't a race against time! At least 5 seconds to keep your sanity intact.",
            "Setting it lower than 5 seconds? You must really like heart palpitations!",
            "Why rush? The crypto market will still be here in 5 seconds."
        ]
        print(f"{Fore.RED}{random.choice(phrases)}{Style.RESET_ALL}")
        exit(1)
    return int_value

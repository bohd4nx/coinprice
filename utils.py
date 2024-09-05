import os


def clear_console():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

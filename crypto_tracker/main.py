import argparse
import time
from crypto_tracker.api_handling import get_crypto_price


def main():
    parser = argparse.ArgumentParser(
        epilog='Commands:\n'
               '  --help               Show this help message and exit.\n'
               '  <coin>               The cryptocurrency to track.\n'
               '  --interval <time>  Interval in seconds to check the price (default: 30).\n'
               '\n'
               'Examples:\n'
               '  crypto_tracker bitcoin\n'
               '  crypto_tracker ethereum --interval 15\n',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('coin', type=str, help='The cryptocurrency to track.')
    parser.add_argument('--interval', type=int, default=30, help='Interval in seconds to check the price (default: 30).')
    args = parser.parse_args()

    coin = args.coin.lower()
    interval = args.interval

    print(f"Tracking {coin.capitalize()} price. Press Ctrl+C to exit.")

    try:
        while True:
            price = get_crypto_price(coin)
            print(f"{coin.capitalize()} price is ${price}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()

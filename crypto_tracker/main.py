from crypto_tracker.cli import parse_arguments
from crypto_tracker.tracker import track_prices


def main():
    args = parse_arguments()
    track_prices(args)


if __name__ == "__main__":
    main()

import time
from api_handling import get_crypto_price
from telegram_bot import send_message
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
tracked_coins = config['Cryptocurrencies']['tracked_coins']


def main():
    while True:
        for coin in tracked_coins.split(','):
            price = get_crypto_price(coin)
            message = f"{coin.capitalize()} price is ${price}"
            send_message(message)
        time.sleep(15)


if __name__ == "__main__":
    main()

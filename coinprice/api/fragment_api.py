import requests
from bs4 import BeautifulSoup


TON = 'https://api.coinpaprika.com/v1/tickers/ton-toncoin'


def get_price():
    # Get the floor price in TON from fragment.com
    url = 'https://fragment.com/numbers?filter=sale'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price_element = soup.find('div', class_='table-cell-value tm-value icon-before icon-ton')
    if price_element:
        price_ton = float(price_element.text.strip().replace(',', ''))
    else:
        price_ton = 0

    # Get the conversion rate from TON to USD
    response = requests.get(TON)
    ton_data = response.json()
    price_usd = price_ton * ton_data['quotes']['USD']['price']

    return price_ton, price_usd

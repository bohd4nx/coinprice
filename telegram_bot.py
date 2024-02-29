import requests
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
bot_token = config['Telegram']['bot_token']
chat_id = config['Telegram']['chat_id']


def send_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=payload)

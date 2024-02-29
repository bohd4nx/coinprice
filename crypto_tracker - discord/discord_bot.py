import discord
from discord.ext import tasks, commands
import configparser
from api_handling import get_crypto_price

config = configparser.ConfigParser()
config.read('config/config.ini')
bot_token = config['Discord']['bot_token']
channel_id = int(config['Discord']['channel_id'])

intents = discord.Intents.default()
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)


@tasks.loop(seconds=15)
async def send_crypto_prices():
    channel = client.get_channel(channel_id)
    tracked_coins = config['Cryptocurrencies']['tracked_coins'].split(',')

    for coin in tracked_coins:
        price = get_crypto_price(coin)
        message = f"{coin.capitalize()} price is ${price}"
        await channel.send(message)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    send_crypto_prices.start()


if __name__ == '__main__':
    client.run(bot_token)

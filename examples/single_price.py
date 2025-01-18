from coinprice.api import get_price

# Simple example of getting a single cryptocurrency price
# Here we're getting Bitcoin price from Binance
coin = "btc"
exchange = "binance"

# Fetch the current price
price = get_price(exchange, coin)

# Display the result with nice formatting
print(f"{coin.upper()} price on {exchange.capitalize()}: ${price:,.2f}")

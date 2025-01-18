from coinprice.api import get_price

# Example of getting prices for multiple cryptocurrencies
# We'll check prices for Bitcoin, Ethereum and Solana

# List of coins we want to check
coins = ["btc", "eth", "sol"]

print("Current prices on Binance:")
print("-" * 30)

# Iterate through our coins list and get price for each
for coin in coins:
    price = get_price("binance", coin)
    print(f"{coin.upper()} price: ${price:,.2f}")

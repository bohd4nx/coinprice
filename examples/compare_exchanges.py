from coinprice.api import get_price

# Example of comparing prices across different exchanges
# This helps to spot price differences between exchanges

# List of exchanges to compare
exchanges = ["binance", "coinbase", "kraken"]
coin = "btc"

print(f"\n{coin.upper()} prices across exchanges:")

# Get and display price from each exchange
for exchange in exchanges:
    try:
        price = get_price(exchange, coin)
        print(f"{exchange.capitalize()}: ${price:,.2f}")
    except Exception as e:
        print(f"{exchange.capitalize()}: Error - {str(e)}")

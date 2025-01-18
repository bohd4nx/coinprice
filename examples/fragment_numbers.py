from coinprice.api import numprice


def track_fragment():
    ton, usd = numprice()
    print(f"Anonymous Numbers floor price: {ton:.2f} TON (${usd:.2f}) | Fee (5%): {ton * 0.05:.2f} TON")


if __name__ == "__main__":
    track_fragment()

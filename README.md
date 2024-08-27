<h2 align="center">
  Crypto Tracker<br/>
  <a href="https://coinprice.bohd4n.dev/" target="_blank">coinprice.bohd4n.dev</a>
</h2>

<p align="center">
 Crypto Tracker is a Python module that allows you to track the prices of cryptocurrencies in real-time. 
You can specify the cryptocurrency you want to track and the module will provide you with live updates on its price.
</p>

<div align="center">

[![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.org/project/coinprice/)
[![Downloads](https://static.pepy.tech/badge/coinprice)](https://pepy.tech/project/coinprice)
[![PyPI format](https://img.shields.io/pypi/format/coinprice.svg)](https://pypi.org/project/coinprice/)
[![PyPI version](https://img.shields.io/pypi/v/coinprice)](https://pypi.org/project/coinprice/)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/coinprice.bohd4n.dev.svg)](https://coinprice.bohd4n.dev/)

</div>

---

## Features

- Track the prices of various cryptocurrencies.
- Flexible Command-line Usage.
- Customizable.
- Set a custom interval for price updates.
- Open-source project.

--- 

## Project Tree


```

crypto_tracker/

│
├── main.py           # Main file to run
├── tracker.py        # Tracking logic and price display
├── cli.py            # Handling command line arguments
├── api/
│ ├── __init__.py     # API package
│ ├── binance.py      # Get price from Binance
│ ├── bybit.py        # Get price from Bybit
│ ├── bitfinex.py     # Get price from Bitfinex
│ └── coinbase.py     # Get price from Coinbase
└── utils.py          # Utilities and helper functions

```

---

![demo](https://github.com/7GitGuru/crypto-tracker/assets/154711952/0df38415-6b97-4d06-ba31-e6a421d520bf)
![demo2](https://github.com/7GitGuru/crypto-tracker/assets/154711952/908a0b26-f6ce-41ae-9a6b-6941ecdf4f76)

---

## Installation

You can install Crypto Tracker using pip:

```
pip install coinprice
```

## Usage

To track the price of a cryptocurrency, simply run the following command:

[//]: # (**[Here you can find a list of all cryptocurrencies you can use.]&#40;https://github.com/7GitGuru/crypto-tracker/blob/main/coin-names.json&#41;**)


```
price <coin>
```

```
price <coin> [--interval time]
```

```
price <coin> [--exchange name] [--interval time]
```

Replace `<coin>` with the cryptocurrency you want to track (e.g., bitcoin, ethereum). You can optionally specify the interval (in seconds) for price updates using the `--interval` flag. By default, the interval is set to 15 seconds.

Example usage:

```
price btc                           Track the price of Bitcoin from all exchanges.
price eth --binance                 Track the price of Ethereum from Binance.
price ltc --coinbase --interval 10  Track the price of Litecoin from Coinbase with a check interval of 10 seconds.
```

### [Check out Telegram version!](https://github.com/7GitGuru/crypto-tracker/tree/telegram)

## Contributing

Contributions to Crypto Tracker are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a [pull request](https://github.com/7GitGuru/crypto-tracker/pulls) on GitHub.

## License

Crypto Tracker is released under the MIT License. See [LICENSE](https://github.com/7GitGuru/crypto-tracker/blob/main/LICENSE) for details.

<h2 align="center">

[Donate](https://www.buymeacoffee.com/bohd4n)

</h2>
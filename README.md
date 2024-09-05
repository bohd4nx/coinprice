<h2 align="center">
  Crypto Tracker <em>(coinprice)</em><br/>
  <a href="https://coinprice.bohd4n.dev/" target="_blank">coinprice.bohd4n.dev</a>
</h2>

<p align="center">
 Crypto Tracker (coinprice) is a Python module that allows you to track the prices of cryptocurrencies in real-time. 
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

- Track the prices of various cryptocurrencies in real-time with updates.
- Display price changes in color depending on rise or decline.
- Flexible command-line interface for easy usage and control.
- Set custom intervals for price updates according to your needs.
- Prices are sorted from highest to lowest for clear comparison.
- Fully customizable and adaptable to your preferences.
- Open-source project for transparency and community input.
- Simple and efficient tracking of crypto prices.

---


![image](https://github.com/user-attachments/assets/2627db02-ff53-47a0-995b-3488a596aa13)
![image](https://github.com/user-attachments/assets/8702fa78-dd51-49e6-bcb8-8f0e7fdff57d)
![image](https://github.com/user-attachments/assets/adf9c68c-6581-4f0e-9280-f9b02cc516a7)

---

## Installation

You can install Crypto Tracker(coinprice) using pip:

```
pip install coinprice
```

## Usage

To track the price of a cryptocurrency, simply run the following command:

```
price <coin>
```

```
price <coin> [-t time]
```

```
price <coin> [--exchange name]
```

```
price <coin> [--exchange name] [-t time]
```

To track the Anonymous Numbers Price, simply run the folowing command:

```
price 8num
```

```
price 8num [-t time]
```

Replace `<coin>` with the cryptocurrency you want to track (e.g., btc, eth). You can optionally specify the interval (in seconds) for price updates using the `-t` or `--interval` flag. By default, the interval is set to 30  seconds.

Example usage:

```
price btc                        Track the price of Bitcoin from all exchanges.
price eth --binance              Track Ethereum price from Binance with default interval.
price ltc --coinbase -t 10       Track Litecoin price on Coinbase in 10 second intervals.
price 8num                       Track Anonymous Telegram Numbers price.
```

## Contributing

Contributions to Crypto Tracker are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a [pull request](https://github.com/7GitGuru/crypto-tracker/pulls) on GitHub.

## License

Crypto Tracker is released under the MIT License. See [LICENSE](https://github.com/bohd4nx/coinprice/blob/main/LICENSE) for details.

<h2 align="center">

[Donate](https://www.buymeacoffee.com/bohd4n)

</h2>
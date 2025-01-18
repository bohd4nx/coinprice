<div align="center">

# 📊 Crypto Tracker
*Real-time cryptocurrency price tracking made simple*

[![PyPI version](https://img.shields.io/pypi/v/coinprice)](https://pypi.org/project/coinprice/)
[![Python Versions](https://img.shields.io/pypi/pyversions/coinprice.svg)](https://pypi.org/project/coinprice/)
[![Downloads](https://static.pepy.tech/badge/coinprice)](https://pepy.tech/project/coinprice)
[![License](https://img.shields.io/github/license/bohd4nx/coinprice)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bohd4nx/coinprice)](https://github.com/bohd4nx/coinprice/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/bohd4nx/coinprice)](https://github.com/bohd4nx/coinprice/issues)

</div>

## 🚀 Features

- **Real-Time Tracking** - Live cryptocurrency price updates
- **Multi-Exchange Support** - Track prices across major exchanges:
  - Binance, Coinbase, Kraken, KuCoin, and more
- **Rich Interface** - Beautiful console output with color-coded changes
- **Custom Intervals** - Flexible update frequency (minimum 5 seconds)
- **Fragment Numbers** - Special support for Telegram's Fragment numbers
- **Error Handling** - Robust error management and fallbacks
- **Easy to Use** - Simple CLI interface
- **Cross-Platform** - Works on Windows, macOS, and Linux

## 📸 Screenshots

<div align="center" style="display: flex; justify-content: space-between; margin: 20px 0;">
  <img src="https://github.com/user-attachments/assets/5cbbfdcb-7c32-40cd-ac22-ee377870adbf" width="49%">
  <img src="https://github.com/user-attachments/assets/debba798-40e9-4d45-bb3f-3d2970410efd" width="49%">
</div>

## 💻 Installation

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

Contributions to Crypto Tracker are welcome! If you find any bugs or have suggestions for new features, please open an [issue](https://github.com/bohd4nx/coinprice/issues) or submit a [pull request](https://github.com/bohd4nx/coinprice/pulls) on GitHub.

## License

Crypto Tracker is released under the MIT License. See [LICENSE](https://github.com/bohd4nx/coinprice/blob/main/LICENSE) for details.

<h2 align="center">
  Crypto Tracker<br/>
  <a href="https://cryptotrack3r.vercel.app/" target="_blank">cryptotrack3r.vercel.app</a>
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

</div>

---
## Features

- Track the prices of various cryptocurrencies.
- Flexible Command-line Usage.
- Customizable.
- Set a custom interval for price updates.
- Open-source project.

--- 

![image](https://github.com/7GitGuru/crypto-tracker/assets/154711952/d5386490-30ca-4bdd-85ec-c0f936cfd5da)

----

## Installation

You can install Crypto Tracker using pip:

```
pip install coinprice
```

## Usage

To track the price of a cryptocurrency, simply run the following command:

**[Here you can find a list of all cryptocurrencies you can use.](https://github.com/7GitGuru/crypto-tracker/blob/main/coin-names.json)**

```
price <coin> [--interval time]
```

Replace `<coin>` with the cryptocurrency you want to track (e.g., bitcoin, ethereum). You can optionally specify the interval (in seconds) for price updates using the `--interval` flag. By default, the interval is set to 15 seconds.

Example usage:

```
price btc                        Track the price of Bitcoin from all exchanges.
price eth --binance              Track the price of Bitcoin from Binance.
price ltc --bybit --interval 10  Track the price of Litecoin from Bybit with a check interval of 10 seconds.
```

### [Check out Telegram version!](https://github.com/7GitGuru/crypto-tracker/tree/telegram)

## Contributing

Contributions to Crypto Tracker are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a [pull request](https://github.com/7GitGuru/crypto-tracker/pulls) on GitHub.

## License

Crypto Tracker is released under the MIT License. See [LICENSE](https://github.com/7GitGuru/crypto-tracker/blob/main/LICENSE) for details.

### Show your support:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/bohd4n)

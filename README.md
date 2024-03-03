# Crypto Tracker

Crypto Tracker is a Python module that allows you to track the prices of cryptocurrencies in real-time. You can specify the cryptocurrency you want to track and the module will provide you with live updates on its price.

## Features

- Track the prices of various cryptocurrencies.
- Set a custom interval for price updates.
- Open-source project.

## Installation

You can install Crypto Tracker using pip:

```
pip install coinprice
```

## Usage

To track the price of a cryptocurrency, simply run the following command:

```
price <coin> [--interval INTERVAL]
```

Replace `<coin>` with the cryptocurrency you want to track (e.g., bitcoin, ethereum). You can optionally specify the interval (in seconds) for price updates using the `--interval` flag. By default, the interval is set to 30 seconds.

Example usage:

```
price bitcoin
price ethereum --interval 15
```

## Contributing

Contributions to Crypto Tracker are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request on GitHub.

## License

Crypto Tracker is released under the MIT License. See [LICENSE](https://github.com/7GitGuru/crypto-tracker/blob/main/LICENSE) for details.


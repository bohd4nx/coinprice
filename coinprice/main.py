import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError

from packaging import version as pkg_version

from coinprice.app.fragment import track_numprice
from coinprice.app.tracker import track_prices
from coinprice.cli import parse_arguments


def check_rich_version():
    required_version = "13.7.1"
    try:
        installed_version = version("rich")
        if pkg_version.parse(installed_version) < pkg_version.parse(required_version):
            print(f"Upgrading 'rich' from version {installed_version} to {required_version}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"rich~={required_version}"])
    except PackageNotFoundError:
        print(f"'rich' not found. Installing version {required_version}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"rich~={required_version}"])


def main(args=None):
    """
    Main entry point for both command-line and module usage.
    
    Args:
        args: Optional parsed arguments. If None, will parse from command line.
    """
    if args is None:
        args = parse_arguments()

    check_rich_version()

    if args.coin == '8num':
        track_numprice(args.interval)
    else:
        track_prices(args)


if __name__ == "__main__":
    main()

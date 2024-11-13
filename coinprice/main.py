import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError

from packaging import version as pkg_version

from coinprice.app.fragment import track_fragment_prices
from coinprice.app.tracker import track_prices
from coinprice.cli import parse_arguments


def main():
    args = parse_arguments()

    if args.coin == '8num':
        track_fragment_prices(args.interval)
    else:
        track_prices(args)


# Function to install or upgrade rich to the required version
def check():
    required_version = "13.7.1"
    try:
        installed_version = version("rich")
        if pkg_version.parse(installed_version) < pkg_version.parse(required_version):
            print(f"Upgrading 'rich' from version {installed_version} to {required_version}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"rich~={required_version}"])
    except PackageNotFoundError:
        print(f"'rich' not found. Installing version {required_version}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"rich~={required_version}"])


check()

if __name__ == "__main__":
    main()

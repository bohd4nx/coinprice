from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='coinprice',
    version='1.6.1',
    author='Bohdan (bohd4nx)',
    author_email='Bohd4n@proton.me',
    description='Coinprice is a command-line tool for tracking cryptocurrency prices across multiple exchanges.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/bohd4nx/coinprice',
    packages=find_packages(exclude=["tests*", "docs*"]),
    install_requires=[
        "requests",
        "rich",
        "colorama",
        "beautifulsoup4",
        "packaging",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    keywords=(
        'cryptocurrency, crypto, coinprice, price, tracking, prices, '
        'finance, binance, coin, exchange, crypto-tracking'
    ),
    project_urls={
        'Documentation': 'https://github.com/bohd4nx/coinprice/blob/main/README.md',
        'Source': 'https://github.com/bohd4nx/coinprice',
        'Bug Tracker': 'https://github.com/bohd4nx/coinprice/issues',
    },

    entry_points={
        'console_scripts': [
            'price = coinprice.main:main',
        ],
    },
    python_requires='>=3.9',
    include_package_data=True,
    zip_safe=False,
)

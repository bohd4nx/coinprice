from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='coinprice',
    version='1.5.3',
    author='Bohdan (bohd4nx)',
    author_email='Bohd4n@proton.me',
    description='CryptoTracker(coinprice) is a command-line tool for tracking cryptocurrency prices across multiple exchanges.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "colorama",
        "beautifulsoup4",
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='cryptocurrency, crypto, coinprice, price, tracking, prices, finance, binance, coin',
    project_urls={
        'GitHub': 'https://github.com/bohd4nx/coinprice/',
        'Documentation': 'https://github.com/bohd4nx/coinprice/blob/main/README.md',
        'Website': 'https://coinprice.bohd4n.dev'
    },
    entry_points={
        'console_scripts': [
            'price = coinprice.main:main',
        ],
    },
    python_requires='>=3.8'

)

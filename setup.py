from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='coinprice',
    version='1.0.0',
    author='Bohdan',
    author_email='bogdan.kov07@outlook.com',
    description='Track cryptocurrency prices.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='cryptocurrency, crypto, bitcoin, ethereum, tracking, prices, finance',
    project_urls={
        'GitHub': 'https://github.com/7GitGuru/crypto-tracker/tree/cmd',
        'Documentation': 'https://github.com/7GitGuru/crypto-tracker/blob/cmd/README.md'
    },
    entry_points={
        'console_scripts': [
            'price = crypto_tracker.main:main',
        ],
    },
    python_requires='>=3.7'

)

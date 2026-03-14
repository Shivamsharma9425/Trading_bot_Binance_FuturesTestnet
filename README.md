# Binance Futures Trading Bot

Simple CLI trading bot for Binance Futures Testnet.

## Setup

1. Clone repo
2. Install dependencies

pip install -r requirements.txt

3. Add API keys to .env

## Run Market Order

python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

## Run Limit Order

python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

Logs stored in logs/bot.log
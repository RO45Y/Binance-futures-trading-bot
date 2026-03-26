# Binance Futures Testnet Trading Bot

A Python CLI application for placing orders on Binance Futures Testnet (USDT-M) with proper logging and error handling.

## Features

- Place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders
- **BUY** and **SELL** support
- Input validation and error handling
- Structured logging to file
- Clean separation of concerns (API layer + CLI layer)

## Setup

### 1. Clone Repository
```bash
git clone &lt;your-repo-url&gt;
cd trade_bot

### 2. Create Virtual Environment
```bash
python -m venv trade_env

### 3. Activate Virtual Environment
```Windows
trade_env\Scripts\activate

```mac/Linux
source trade_env/bin/activate


### 4. Install Dependencies
pip install -r requirements.txt

### 5. Configure API Keys

Create bot/.env file:
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here

1. Get Testnet API Keys:
2. Go to https://testnet.binancefuture.com
3. Register and activate account
4. Go to API Management
5. Create new API key


### Usage

1. Place Market Order
python -m bot.cli place -s ETHUSDT --side BUY -t MARKET -q 0.02

2. Place Limit Order
python -m bot.cli place -s ETHUSDT --side BUY -t LIMIT -q 0.02 -p 2000

3. Place Stop-Limit Order (Bonus)
python -m bot.cli place -s ETHUSDT --side SELL -t STOP-LIMIT -q 0.02 -p 1790 --stop-price 1800

4. Check Account Balance
python -m bot.cli balance




CLI Options

| Option         | Short | Description                                  | Required            |
| -------------- | ----- | -------------------------------------------- | ------------------- |
| `--symbol`     | `-s`  | Trading pair (e.g., BTCUSDT, ETHUSDT)        | Yes                 |
| `--side`       |       | BUY or SELL                                  | Yes                 |
| `--type`       | `-t`  | MARKET, LIMIT, or STOP-LIMIT                 | Yes                 |
| `--qty`        | `-q`  | Order quantity                               | Yes                 |
| `--price`      | `-p`  | Price (required for LIMIT and STOP-LIMIT)    | For LIMIT/STOPLIMIT |
| `--stop-price` |       | Stop trigger price (required for STOP-LIMIT) | For STOPLIMIT       |


Project Structure

trade_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   ├── cli.py             # CLI entry point
│   └── .env               # API credentials (ignored by git)
├── trade_env/             # Virtual environment
├── .gitignore
├── requirements.txt
└── README.md


Comman Errors:

| Error                                         | Solution                                                        |
| --------------------------------------------- | --------------------------------------------------------------- |
| `Invalid API-key, IP, or permissions`         | Whitelist your IP in Binance API settings or use "Unrestricted" |
| `Limit price can't be higher than X`          | Set limit price below current market price for BUY orders       |
| `Order's notional must be no smaller than 20` | Increase quantity or price to reach 20 USDT minimum             |
| `Precision is over the maximum`               | Reduce quantity decimal places (e.g., 0.001 instead of 0.0001)  |
| `ImportError: No module named 'bot'`          | Run from root `trading_bot/` folder, use `python -m bot.cli`    |
# Binance Futures Testnet Trading Bot

A Python CLI application for placing orders on Binance Futures Testnet (USDT-M) with proper logging and error handling.

## Features

- Place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders
- **BUY** and **SELL** support
- Input validation and error handling
- Structured logging to file
- Clean separation of concerns (API layer + CLI layer)



## 📦 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/RO45Y/Binance-futures-trading-bot.git
cd trade_bot
```

### 2. Create Virtual Environment
```bash
python -m venv trade_env
```

### 3. Activate Virtual Environment

**Windows**
```bash
trade_env\Scripts\activate
```

**macOS / Linux**
```bash
source trade_env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file inside the `bot/` folder:

```env
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

#### 🔑 Get Testnet API Keys
1. Go to https://testnet.binancefuture.com  
2. Register and activate your account  
3. Navigate to API Management  
4. Create a new API key  

---

## ⚙️ Usage

### 📌 Place Market Order
```bash
python -m bot.cli place -s ETHUSDT --side BUY -t MARKET -q 0.02
```

### 📌 Place Limit Order
```bash
python -m bot.cli place -s ETHUSDT --side BUY -t LIMIT -q 0.02 -p 2000
```

### 📌 Place Stop-Limit Order
```bash
python -m bot.cli place -s ETHUSDT --side SELL -t STOP-LIMIT -q 0.02 -p 1790 --stop-price 1800
```

### 📌 Check Account Balance
```bash
python -m bot.cli balance
```

---

## 🧩 CLI Options

| Option         | Short | Description                                  | Required            |
|----------------|------|----------------------------------------------|---------------------|
| --symbol       | -s   | Trading pair (e.g., BTCUSDT, ETHUSDT)        | Yes                 |
| --side         |      | BUY or SELL                                  | Yes                 |
| --type         | -t   | MARKET, LIMIT, STOP-LIMIT                    | Yes                 |
| --qty          | -q   | Order quantity                               | Yes                 |
| --price        | -p   | Price (for LIMIT & STOP-LIMIT)               | Conditional         |
| --stop-price   |      | Stop trigger price (for STOP-LIMIT)          | Conditional         |

---

## 📁 Project Structure

```
trade_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── cli.py
│   └── .env
├── trade_env/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚠️ Common Errors & Fixes

| Error                                         | Solution                                                        |
|----------------------------------------------|-----------------------------------------------------------------|
| Invalid API-key, IP, or permissions           | Whitelist IP or set API restrictions to Unrestricted           |
| Limit price can't be higher than X            | Set lower price for BUY orders                                 |
| Order's notional must be no smaller than 20   | Increase quantity or price (min 20 USDT)                       |
| Precision is over the maximum                 | Reduce decimal places                                          |
| ImportError: No module named 'bot'            | Run from root folder using python -m bot.cli                  |

---

## 💡 Notes
- Use Binance Testnet for testing  
- Never expose your API keys  
- .env file should be added to .gitignore  

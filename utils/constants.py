# Default user setup
DEFAULT_INITIAL_BALANCE = 100000.0  # ₹1,00,000

# Preloaded stock symbols for simulation

DEFAULT_STOCKS = [
    {"symbol":"TCS","name":"Tata Consultancy Services","price": 3450.0},
    {"symbol": "INFY", "name": "Infosys Ltd", "price": 1540.0},
    {"symbol": "RELIANCE", "name": "Reliance Industries", "price": 2410.0},
    {"symbol": "HDFCBANK", "name": "HDFC Bank", "price": 1585.0},
    {"symbol": "ITC", "name": "ITC Ltd", "price": 460.0},
    {"symbol": "SBIN", "name": "State Bank of India", "price": 735.0},
]

# Market update frequency (seconds)
MARKET_UPDATE_INTERVAL = 3
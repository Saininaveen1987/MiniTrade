import time
import threading
from utils.constants import DEFAULT_STOCKS
from models.stock import Stock
from typing import Optional

# class Market:
#     def __init__(self, stocks: list[Stock]):
#         self.stocks = {stock.symbol: stock for stock in stocks}

class Market:
    def __init__(self, stocks: Optional[list[Stock]] = None):
        if stocks is None:
            #Create stock object from constants
            self.stocks = {s["symbol"]: Stock(**s) for s in DEFAULT_STOCKS}
        else:
            self.stocks = {stock.symbol:stock for stock in stocks}

    def start_market(self):
        """Simulate Market Price Updates in the background"""
        def run():
            while True:
                for stock in self.stocks.values():
                    stock.update_price()
                time.sleep(3)
        threading.Thread(target=run, daemon=True).start
    
    def get_price(self, symbol: str) -> float | None:
        stock = self.stocks.get(symbol)
        return stock.price if stock else None
    
    def list_stocks(self):
        return [str(stock) for stock in self.stocks.values()]
    
        
import time
import threading
from models.stock import Stock

class Market:
    def __init__(self, stocks: list[Stock]):
        self.stocks = {stock.symbol: stock for stock in stocks}

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
    
        
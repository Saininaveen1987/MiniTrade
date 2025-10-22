import random

class Stock:
    def __init__(self, symbol:str, name:str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price

    def update_price(self):
        """Randomly update price to simulate Market movement"""
        change = random.uniform(-0.02, 0.02)
        self.price = round(self.price * (1+ change),2)

    def __str__(self):
        return f"{self.symbol} ({self.name}): ₹{self.price})"
        
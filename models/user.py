from models.portfolio import Portfolio

class User:
    def __init__(self, username:str, balance:float = 100000.0):
        self.username = username
        self.balance = balance
        self.portfolio = Portfolio()
        self.order_history = []

    def __str__(self):
        return f"User ({self.username}, Balance: ₹{self.balance:.2f})"
    
    def show_portfolio(self, market):
        self.portfolio.summary(market)
    
    def add_order(self,order):
        self.order_history.append(order)
        
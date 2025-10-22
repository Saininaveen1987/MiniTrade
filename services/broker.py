from models.order import Order
from services.trade_engine import TradeEngine

class Broker:
    def __init__(self, market):

        self.market = market
        self.trade_engine = TradeEngine(market) 
        self.order_book = []

    def place_order(self,user, symbol, qty, order_type):
        price = self.market.get_price(symbol)
        if price is None:
            print(f"❌ Symbol {symbol} not found in market.")
            return
        
        order = Order(user, symbol, qty, order_type, price)
        print(f"Received order: {order}")

        #validate before execution
        if not self._validate_order(user,order):
            order.status = "REJECTED"
            print(f"⚠️  Order rejected due to insufficient funds/holdings.")
        
        #execute through trade engine
        self.trade_engine.execute_order(order)
        self.order_book.append(order)
        user.add_order(order)

    def _validate_order(self, user, order):
        if order.order_type == "BUY":
            total_cost = order.price * order.qty
            return user.balance >= total_cost
        elif order.order_type == "SELL":
            held = user.portfolio.get(order.symbol, {}).get("qty",0)
            return held>= order.qty
        return False
class TradeEngine:
    def __init__(self, market):
        self.market = market

    def execute_order(self, order):
        price = self.market.get_price(order.symbol)
        user = order.user

        if order.order_type == "BUY":
            cost = price*order.qty
            user.balance -= cost
            # self._update_portfolio_buy(user, order.symbol, order.qty, price)
            user.portfolio.add_buy(order.symbol, order.qty, price) 
            order.status = "FILLED"
        
        elif order.order_type == "SELL":
            proceeds = price*order.qty
            user.balance += proceeds
            # self._update_portfolio_sell(user, order.symbol, order.qty)
            user.portfolio.add_sell(order.symbol, order.qty)
            order.status = "FILLED"

        print(f"✅ Executed {order.order_type} {order.qty} {order.symbol} @ ₹{price}")


    # def _update_portfolio_buy(self, user, symbol, qty, price):
    #     """Average out the  new purchase with existing holdings"""
    #     holding = user.portfolio.get(symbol, {"qty":0, "avg_price":0})
    #     total_qty = holding["qty"] + qty
    #     total_cost = holding["qty"]*holding["avg_price"] + qty*price
    #     new_avg = total_cost / total_qty
    #     user.portfolio [symbol] = {"qty": total_qty, "avg_price":round(new_avg,2)}


    # def _update_portfolio_sell(self, user, symbol, qty):
    #     """Reduce or remove completely from existing holdings"""
    #     holding = user.portfolio.get(symbol)
    #     if not holding:
    #         return
    #     holding["qty"] -= qty

    #     if holding["qty"] <= 0:
    #         del user.portfolio

    
        
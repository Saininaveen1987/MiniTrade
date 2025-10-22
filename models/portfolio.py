
class Portfolio:
    def __init__(self):
        # {symbol: {"qty": int, "avg_price":float}}
        self.holdings = {}


    def add_buy(self, symbol, qty, price):
        holding = self.holdings.get(symbol, {"qty": 0 , "avg_price":0})
        total_qty = holding["qty"] + qty
        total_cost = holding["qty"] * holding["avg_price"] + qty * price
        new_avg = total_cost / total_qty
        self.holdings [symbol] = {"qty": total_qty, "avg_price": round(new_avg, 2)} 

    def add_sell(self, symbol, qty):
        holding = self.holdings.get(symbol)
        if not holding:
            return
        holding[qty] -= qty
        if holding[qty] <=0:
            del self.holdings[symbol]
        

    def compute_pnl(self, market):
        """Returns overall & perstock P&L based on live Market Prices"""
        pnl_data = {}
        total_pnl = 0
        for symbol,data in self.holdings.items():
            market_price = market.get_price(symbol)
            pnl = (market_price - data["avg_price"]) * data["qty"]
            pnl_data[symbol] = {
                "qty": data["qty"],
                "avg_price": data["avg_price"],
                "market_price": market_price,
                "pnl": round(pnl, 2),
            }
            total_pnl += pnl
        return pnl_data, round(total_pnl,2)

    def summary(self, market):
        pnl_data, total_pnl = self.compute_pnl(market)
        print("\n Portfolio Summary: ")
        for sym,info in pnl_data.items():
            print(f"{sym}: {info["qty"]} @ ₹{info['avg_price']} | "
                  f"Live ₹ {info['market_price']} | P&L ₹{info['pnl']}")
        print(f"💰 Total P&L: ₹{total_pnl:.2f}")
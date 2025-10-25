from utils.formatter import format_currency

def show_market(market):
    print("\n" + "="*40)
    print("📈 LIVE MARKET PRICES")
    print("="* 40)
    print(f"{'Symbol':<10} | {'Price':>10}")
    print("-"*25)
    for symbol, stock in market.stocks.items():
        print(f"{symbol:<10} | {format_currency(stock.price):>10}")
    print("-"*25)

def show_portfolio(user, market):
    print("\n" + "="*50)
    print("📁 YOUR PORTFOLIO")
    print("="*50)
    print(f"{'Symbol':<10} | {'Qty':>5} | {'Avg Price':>10} | {'LTP':>10} | {'P&L':>10}")
    print("-"*50)
    total_pnl = 0
    for symbol, holding in user.portfolio.holdings.items():
        qty = holding['qty']
        avg_price = holding['avg_price']
        ltp = market.get_price(symbol)
        pnl = (ltp - avg_price)* qty
        total_pnl += pnl
        print(f"{symbol:<10} | {qty:>5} | {format_currency(avg_price):>10} | {format_currency(ltp):>10} | {format_currency(pnl):>5}")
    print("-"*50)
    print(f"Total P&L: {format_currency(total_pnl)}")
    print("="*50)

def show_order_history(user):
    print("\n" + "="*60)
    print("📜 ORDER HISTORY")
    print("="*60)
    print(f"{'ID':<8} | {'Type':<4} | {'Symbol':<6} | {'Qty':>5} | {'Price':>10} | {'Status':<6} | {'Time':<16}")
    print("-"*60)
    for order in user.order_history:
        print(f"{order.id:<8} | {order.order_type:<4} | {order.symbol:<6} | {order.qty:>5} | {order.price:>10.2f} | {order.status:<6} | {order.timestamp.strftime('%Y-%m-%d %H:%M'):<16}")
    print("="* 60)    

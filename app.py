from models.user import User
from models.stock import Stock
from services.market import Market
from services.broker import Broker
from services.datastore import Datastore
import time, os

#Create Some Stocks

stocks = [
    Stock ("TCS", "Tata Consultancy Services", 3500),
    Stock ("INFY", "Infosys", 1550),
    Stock ("HDFCBANK", "HDFC BANK", 1580),
]

# start the Market
market = Market(stocks)
market.start_market()

#Create broker and User

broker = Broker(market)
store = Datastore()

# user = User("Naveen", 200000)

username = "Naveen"
user_data = store.load_user(username)

if user_data:
    print(f"Loading existing User: {username}")
    user = User(username, user_data["balance"])
    user.portfolio.holdings = user_data["holdings"]
else:
    print(f"🆕 Creating new user: {username}")
    user = User(username)


time.sleep(1)

print("\n Market Snapshot")
for s in market.list_stocks():
    print(s)

# place a few orders

# broker.place_order(user, "TCS", 10, "BUY")
# broker.place_order(user, "TCS", 5, "SELL")

# print("\n📒 Portfolio:")
# print(user.portfolio)
# print(f"💰 Balance: ₹{user.balance:.2f}")



broker.place_order(user, "TCS", 10, "BUY")
time.sleep(1)
broker.place_order(user, "INFY", 5, "BUY")

user.show_portfolio(market)
store.save_user(user)

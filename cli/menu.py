from datetime import datetime
from cli.views import show_market, show_portfolio, show_order_history

def main_menu(datastore):
    while True:
        print("\n" + "="*40)
        print("🏦 Welcome to MiniTrade")
        print("="*40)
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            username = input("Enter Username: ").strip()
            user = datastore.load_user(username)
            if user: 
                return user
            else:
                print("❌ User not found!")
        elif choice == '2':
            username = input("Choose Username: ").strip()
            user = datastore.create_user(username)
            return user
        elif choice == '3':
            print("Goodbye! 👋")
            exit()
        else:
            print("❌ Invalid choice. Try again.")

def dashboard_menu(user, broker, market, datastore):
    while True:
        print("\n" + "="*50)
        print(f"MINI TRADE DASHBOARD  |  User: {user.username}")
        print("="*50)
        print("1. View Market Prices")
        print("2. View Portfolio")
        print("3. Place Order (Buy/Sell)")
        print("4. View Order History")
        print("5. Deposit / Withdraw Funds")
        print("6. Save & Logout")
        choice = input("Enter your choice: ").strip()

        if choice=='1':
            show_market(market)
        
        elif choice == '2':
            show_portfolio(user, market)
            
        elif choice == '3':
            place_order_cli(user,broker,market)
            
        elif choice == '4':
            show_order_history(user)
            
        elif choice == '5':
            manage_funds(user)
            
        elif choice == '6':
            datastore.save_user(user)
            print("✅ Data saved successfully! Logging out...")
            break

        else:
            print("❌ Invalid choice. Try again.")

def place_order_cli(user, broker, market):
    print("\n🛒 PLACE ORDER")
    order_type = input("Enter Order Type : (BUY/SELL)").strip().upper()
    symbol = input("Enter Stock Symbol: ").strip().upper()
    qty = int(input("Enter quantity: "))
    confirm = input(f"Confirm {order_type} {qty} {symbol}? (Y/N): ").strip().upper()
    if confirm == 'Y':
        broker.place_order(user, symbol, qty, order_type)
    else:
        print("❌ Order cancelled.")

def manage_funds(user):
    print("\n 💰 FUNDS MANAGEMENT")
    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    choice = input("Enter choice: ").strip()
    amount = float(input("Enter amount: "))
    if choice == '1':
        user.balance += amount
        print(f" ✅ Deposited ₹{amount}. New Balance: ₹{user.balance}")
    elif choice == '2':
        if amount <= user.balance:
            user.balance -= amount
            print(f"✅ Withdrawn ₹{amount},New Balance: ₹{user.balance}")
        else:
            print("❌ Insufficient balance.")
    else:
        print("❌ invalid Choice.")
        


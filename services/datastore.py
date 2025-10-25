import json
from pathlib import Path
from models.user import User
from models.order import Order
from models.portfolio import Portfolio
from utils.constants import DEFAULT_INITIAL_BALANCE

class Datastore:
    def __init__(self, filename="data.json") :
        self.file = Path(filename)
        if not self.file.exists():
            self.file.write_text(json.dumps({"users": []}, indent=2))

    
    def save_user(self, user):
        """Save user state (balance, holdings, orders)."""
        data = json.loads(self.file.read_text())
        user_data = {
            "username": user.username,
            "balance": user.balance,
            "holdings": user.portfolio.holdings,
            "orders": [o.to_dict() for o in user.order_history]
        }
        # overwrite or add
        data["users"] = [u for u in data["users"]if u["username"] != user.username]
        data["users"].append(user_data)
        # print("DEBUG save_user data:", user_data)
        self.file.write_text(json.dumps(data, indent=2))
    
    def load_user(self, username):
        """Load user from your file"""
        data = json.loads(self.file.read_text())
        for u in data["users"]:
            if u["username"] == username:
                user = User(username= u["username"], balance=u["balance"])
                user.portfolio = Portfolio()
                user.portfolio.holdings = u.get ("holdings", {})
                user.order_history = [Order.from_dict(o) for o in u.get("orders", [])]
                return user
        return None
    
    def create_user(self, username):
        """Create and save a new user with default balance & empty portfolio."""
        # Check if already exists
        existing = self.load_user(username)
        if existing:
            print(f" User '{username}' already exists. Please log in instead.")
            return None
        user = User(username=username, balance=DEFAULT_INITIAL_BALANCE)
        user.portfolio = Portfolio()
        user.order_history = []
        
        self.save_user(user)
        print(f" User '{username}' created successfully with ₹ {DEFAULT_INITIAL_BALANCE:,.2f} balance.")
        return user
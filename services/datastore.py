import json
from pathlib import Path

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
                return u
        return None
import uuid
from datetime import datetime

class Order:
    def __init__(self, user, symbol:str, qty:int, order_type: str, price: float | None = None, timestamp=None):
        self.id = str(uuid.uuid4())
        self.user = user
        self.symbol = symbol
        self.qty = qty
        self.order_type = order_type.upper()
        self.price = price
        self.status = "PENDING"
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return (f"[{self.status}] {self.order_type} {self.qty} x {self.symbol}"
                f"@ ₹ {self.price if self.price else "MARKET"} ({self.id[:8]})")
    
    def to_dict(self):
        """Return a Json Dict representation"""
        return {
            "id": self.id,
            "symbol": self.symbol,
            "qty": self.qty,
            "order_type": self.order_type,
            "price": self.price,
            "status": self.status,
            "timestamp": self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data, user=None):
        """Recreate an Order Object from a dict."""
        order = cls(
            user = user,
            symbol = data.get("symbol"),
            qty=data.get("qty"),
            order_type=data.get("order_type"),
            price=data.get("price")
        )
        order.id = data.get("id", str(uuid.uuid4()))
        order.status = data.get("status", "PENDING")
        ts = data.get("timestamp") or data.get("Timestamp")
        if ts:
            try:
                order.timestamp = datetime.fromisoformat(ts)
            except ValueError:
                order.timestamp = datetime.now
        return order
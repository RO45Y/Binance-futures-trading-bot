def validate_symbol(symbol: str) -> str:
    if not symbol or len(symbol) < 4:
        raise ValueError("Invalid symbol format (e.g., BTCUSDT)")
    return symbol.upper()

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT", "STOP-LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP-LIMIT")
    return order_type

def validate_stop_price(stop_price: float, order_type: str) -> float:
    if order_type == "STOP-LIMIT" and (stop_price is None or stop_price <= 0):
        raise ValueError("Stop price required and must be positive for STOP-LIMIT orders")
    return stop_price

def validate_quantity(qty: float) -> float:
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    return qty

def validate_price(price: float, order_type: str) -> float:
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price required and must be positive for LIMIT orders")
    return price
from .client import BinanceFuturesClient
from .validators import *
from .logging_config import setup_logging

logger = setup_logging()

class OrderManager:
    def __init__(self):
        self.client = BinanceFuturesClient()
    
    def place_order(self, symbol: str, side: str, order_type: str, 
                quantity: float, price: float = None, stop_price: float = None):
        """Main order placement with validation and logging"""
        try:
            # Validate inputs
            symbol = validate_symbol(symbol)
            side = validate_side(side)
            order_type = validate_order_type(order_type)
            quantity = validate_quantity(quantity)
            price = validate_price(price, order_type)
            stop_price = validate_stop_price(stop_price, order_type)
            
            # Log request
            log_msg = (f"ORDER REQUEST | Symbol: {symbol} | Side: {side} | "
                    f"Type: {order_type} | Qty: {quantity} | Price: {price}")
            if stop_price:
                log_msg += f" | StopPrice: {stop_price}"
            logger.info(log_msg)
            
            # Place order
            response = self.client.place_order(symbol, side, order_type, quantity, price, stop_price)
            
            # Log success
            logger.info(f"ORDER SUCCESS | OrderID: {response.get('orderId')} | "
                    f"Status: {response.get('status')} | "
                    f"ExecutedQty: {response.get('executedQty')}")
            
            
            logger.info(f"FULL RESPONSE: {response}")

            return {
                'success': True,
                'order_id': response.get('algoId') or response.get('orderId') or 'N/A',
                'status': response.get('algoStatus') or response.get('status') or 'NEW',
                'symbol': response.get('symbol'),
                'side': response.get('side'),
                'type': response.get('orderType') or order_type,
                'quantity': response.get('quantity'),
                'executed_qty': response.get('executedQty') or '0',
                'avg_price': response.get('avgPrice') or '0',
                'stop_price': stop_price,
                'trigger_price': response.get('triggerPrice'),
                'raw_response': response
            }
            
        except Exception as e:
            logger.error(f"ORDER FAILED | Error: {str(e)}")
            return {'success': False, 'error': str(e)}
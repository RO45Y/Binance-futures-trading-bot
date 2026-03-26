import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_API_SECRET')
        self.base_url = "https://testnet.binancefuture.com"
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API credentials not found in environment variables")
        
        self.client = Client(self.api_key, self.api_secret, testnet=True)
        self.client.FUTURES_URL = self.base_url + "/fapi"
    
    def place_order(self, symbol: str, side: str, order_type: str, 
                quantity: float, price: float = None, stop_price: float = None):
        """Place order on Binance Futures Testnet"""
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'quantity': quantity,
            }
            
            if order_type == "MARKET":
                params['type'] = 'MARKET'
            elif order_type == "LIMIT":
                params['type'] = 'LIMIT'
                params['price'] = price
                params['timeInForce'] = 'GTC'
            elif order_type == "STOP-LIMIT":
                params['type'] = 'STOP'  
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = 'GTC'
            
            response = self.client.futures_create_order(**params)
            return response
            
        except Exception as e:
            raise Exception(f"Error placing order: {str(e)}")
        
    def get_account_info(self):
        """Get account balance/info"""
        return self.client.futures_account()
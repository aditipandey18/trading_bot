from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(1234567890, 0987654321, testnet=testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
        except Exception as e:
            raise RuntimeError(f"Order failed: {e}")

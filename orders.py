import logging
from .client import BinanceClient

def execute_order(api_key, api_secret, symbol, side, order_type, quantity, price=None):
    client = BinanceClient(1234567890, 0987654321)
    logging.info(f"Placing {order_type} {side} order for {quantity} {symbol} at {price if price else 'MARKET'}")
    response = client.place_order(symbol, side, order_type, quantity, price)
    logging.info(f"Order response: {response}")
    return response

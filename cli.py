import typer
from .orders import execute_order
from .validators import validate_side, validate_order_type
import logging
from .logging_config import *

app = typer.Typer()

@app.command()
def order(
    api_key: str,
    api_secret: str,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    side = validate_side(side)
    order_type = validate_order_type(order_type)

    try:
        response = execute_order(api_key, api_secret, symbol, side, order_type, quantity, price)
        typer.echo(f"✅ Order placed successfully: {response}")
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        typer.echo(f"❌ Failed to place order: {e}")

if __name__ == "__main__":
    app()

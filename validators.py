import typer

def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise typer.BadParameter("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise typer.BadParameter("Order type must be MARKET or LIMIT")
    return order_type

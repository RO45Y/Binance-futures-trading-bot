import typer
from typing import Optional
from bot.orders import OrderManager
from bot.logging_config import setup_logging

app = typer.Typer(help="Binance Futures Testnet Trading Bot")
logger = setup_logging()

@app.command()
def place(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading pair (e.g., BTCUSDT)"),
    side: str = typer.Option(..., "--side", help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", "-t", help="MARKET, LIMIT, or STOP-LIMIT"),
    quantity: float = typer.Option(..., "--qty", "-q", help="Order quantity"),
    price: Optional[float] = typer.Option(None, "--price", "-p", help="Price (required for LIMIT and STOP-LIMIT)"),
    stop_price: Optional[float] = typer.Option(None, "--stop-price", help="Stop price (required for STOP-LIMIT)")
):
    """Place a new order"""
    
    # Display order summary
    typer.echo(f"\n📋 ORDER SUMMARY:")
    typer.echo(f"   Symbol: {symbol.upper()}")
    typer.echo(f"   Side: {side.upper()}")
    typer.echo(f"   Type: {order_type.upper()}")
    typer.echo(f"   Quantity: {quantity}")
    if price:
        typer.echo(f"   Price: {price}")
    if stop_price:
        typer.echo(f"   Stop Price: {stop_price}")
    
    confirm = typer.confirm("\nProceed?")
    if not confirm:
        typer.echo("❌ Cancelled")
        raise typer.Exit()
    
    manager = OrderManager()
    result = manager.place_order(symbol, side, order_type, quantity, price, stop_price)
    
    if result['success']:
        typer.echo("✅ ORDER PLACED!")
        typer.echo(f"   Algo/Order ID: {result.get('order_id', 'N/A')}")
        typer.echo(f"   Status: {result.get('status', 'NEW')}")
        typer.echo(f"   Symbol: {result.get('symbol')}")
        typer.echo(f"   Side: {result.get('side')}")
        typer.echo(f"   Type: {result.get('type')}")
        typer.echo(f"   Quantity: {result.get('quantity')}")
        if result.get('stop_price'):
            typer.echo(f"   Stop Price: {result['stop_price']}")
        if result.get('trigger_price'):
            typer.echo(f"   Trigger Price: {result['trigger_price']}")
    else:
        typer.echo(f"❌ FAILED: {result['error']}")


@app.command()
def balance():
    """Check account balance"""
    manager = OrderManager()
    try:
        logger.info("BALANCE CHECK REQUESTED")  
        account = manager.client.get_account_info()
        typer.echo("\n💰 ACCOUNT BALANCE:")
        for asset in account['assets']:
            if float(asset['walletBalance']) > 0:
                typer.echo(f"   {asset['asset']}: {asset['walletBalance']}")
        logger.info("BALANCE CHECK SUCCESS")  
    except Exception as e:
        logger.error(f"BALANCE CHECK FAILED | Error: {e}") 
        typer.echo(f"❌ Error fetching balance: {e}")

if __name__ == "__main__":
    app()
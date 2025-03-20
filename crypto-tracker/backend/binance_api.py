from binance import AsyncClient
import os
from dotenv import load_dotenv

load_dotenv()

async def get_binance_price(symbol: str):
    client = await AsyncClient.create(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_SECRET_KEY")
    )
    ticker = await client.get_symbol_ticker(symbol=f"{symbol}USDT")
    await client.close_connection()
    return float(ticker["price"])
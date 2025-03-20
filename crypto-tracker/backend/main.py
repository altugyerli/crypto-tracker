from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from binance_api import get_binance_price
from coinmarketcap import get_trending_coins
from ai_analysis import analyze_sentiment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price/{symbol}")
async def get_price(symbol: str):
    price = await get_binance_price(symbol)
    return {"symbol": symbol, "price": price}

@app.get("/trending")
async def trending():
    return get_trending_coins()

@app.post("/analyze")
async def analyze(texts: list):
    return analyze_sentiment(texts)
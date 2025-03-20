import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_trending_coins():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/latest"
    headers = {"X-CMC_PRO_API_KEY": os.getenv("COINMARKETCAP_API_KEY")}
    response = requests.get(url, headers=headers)
    return response.json()
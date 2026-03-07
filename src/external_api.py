import os
from dotenv import load_dotenv
import requests

load_dotenv()

def convert_to_rub(transactions_sum, currency):
    url = "https://api.apilayer.com/exchangerates_data/latest"
    api_key = os.getenv("API_KEY")
    payload = {
        "base": currency,
        "symbols": "RUB"
    }
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers, params=payload)

    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        rate = result["rates"]["RUB"]
        convertation_result = rate * transactions_sum
        return convertation_result
    else:
        return 0.0

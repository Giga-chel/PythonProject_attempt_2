import json
from src.external_api import convert_to_rub

def financial_transactions(file_path: str) -> list:
    """Функция с данными о финансовых транзакциях"""
    try:
        with open(file_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        data = []
    except FileNotFoundError:
        data = []
    if not isinstance(data, list):
        data = []
    return data

def get_transactions_amount_in_rub(transaction: dict) -> float:
    """Функция перевода в рублях"""
    amount = float(transaction['operationAmount']['amount'])
    code = transaction['operationAmount']['currency']['code']
    if code == "RUB":
        return amount
    elif code == "USD" or code == "EUR":
        return convert_to_rub(amount, code)
    else:
        return 0.0

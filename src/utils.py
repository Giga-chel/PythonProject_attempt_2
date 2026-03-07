import json

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
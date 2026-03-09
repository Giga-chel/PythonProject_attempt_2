import json
import logging
import os

from src.external_api import convert_to_rub

app_logger = logging.getLogger(__name__)
os.makedirs("logs", exist_ok=True)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.INFO)


def financial_transactions(file_path: str) -> list:
    """Функция с данными о финансовых транзакциях"""
    try:
        with open(file_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        app_logger.error("Невозможно декодировать(преобразовать) данные")
        data = []
    except FileNotFoundError:
        app_logger.error(f"{file_path} не найден")
        data = []
    if not isinstance(data, list):
        data = []
    return data


def get_transactions_amount_in_rub(transaction: dict) -> float:
    """Функция перевода в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        app_logger.info("Перевод в рублях")
        return amount
    elif code == "USD" or code == "EUR":
        app_logger.info(f"Конвертация валюты {code}: {amount}")
        return convert_to_rub(amount, code)
    else:
        app_logger.warning(f"Неподдерживаемый код валюты: {code}")
        return 0.0

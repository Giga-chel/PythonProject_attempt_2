from datetime import datetime

"""Используем встроенный модуль datetime для функции get_date"""
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_info: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
    parts = mask_info.split()

    number = parts[-1]

    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция, которая принимает и возвращает строку с датой"""
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")

    result = date_obj.strftime("%d.%m.%Y")

    return result

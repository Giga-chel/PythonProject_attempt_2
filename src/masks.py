import logging
import os

app_logger = logging.getLogger(__name__)
os.makedirs('logs', exist_ok=True)
file_handler = logging.FileHandler('logs/masks.log', 'w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.INFO)

def get_mask_card_number(card_number: str | int) -> str:
    """Функция, которая маскирует номер карты"""
    card_num_in_str = str(card_number)

    if len(card_num_in_str) != 16:
        app_logger.error("Ошибка: Номер карты должен содержать 16 цифр")
        raise ValueError("Ошибка: Номер карты должен содержать 16 цифр")

    visible_start = card_num_in_str[:6]
    visible_end = card_num_in_str[-4:]

    stars = "*" * (len(card_num_in_str) - 10)

    mask_full = visible_start + stars + visible_end

    mask_blocks = [mask_full[i : i + 4] for i in range(0, len(mask_full), 4)]
    app_logger.info(" ".join(mask_blocks))
    return " ".join(mask_blocks)


def get_mask_account(acc_number: str | int) -> str:
    """Функция, которая маскирует номер счета"""
    acc_str = str(acc_number)

    if len(acc_str) != 20:
        app_logger.error("Ошибка: Номер счета должен содержать 20 цифр")
        raise ValueError("Ошибка: Номер счета должен содержать 20 цифр")

    visible_end = acc_str[-4:]

    app_logger.info("** " + visible_end)
    return "** " + visible_end

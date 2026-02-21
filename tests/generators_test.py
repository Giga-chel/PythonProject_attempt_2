from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

"""Тесты для модуля generators"""

# --- filter_by_currency ---


def test_filter_by_currency_usd(test_transactions):
    """Тест с успешным отфильтровыванием."""
    gen_result = filter_by_currency(test_transactions, "USD")
    result_list = list(gen_result)
    assert len(result_list) == 3
    assert result_list[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_empty_result(test_transactions):
    """Тест с отсутствующими транзакциями."""
    gen_result = filter_by_currency(test_transactions, "EUR")
    result_list = list(gen_result)
    assert len(result_list) == 0


def test_filter_by_currency_empty_input():
    """Тест с пустыми транзакциями."""
    gen_result = filter_by_currency([], "")
    result_list = list(gen_result)
    assert len(result_list) == 0


# --- transaction_descriptions ---


def test_transaction_descriptions(test_transactions):
    """Получение описания."""
    gen_result = transaction_descriptions(test_transactions)
    result_list = list(gen_result)
    assert result_list[0] == "Перевод организации"
    assert len(result_list) == 5


# --- card_number_generator


def test_card_number_generator_range():
    """Тест генератора карт."""
    gen_result = card_number_generator(1, 3)
    result_list = list(gen_result)
    assert len(result_list) == 3
    assert result_list[0] == "0000 0000 0000 0001"

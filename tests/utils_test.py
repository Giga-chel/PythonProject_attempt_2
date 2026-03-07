import os

from src.utils import financial_transactions, get_transactions_amount_in_rub
from unittest.mock import patch

# --- financial_transactions ---

def test_financial_transactions_success():
    """Тест функции с финансовыми транзакциями на успех"""
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    result = financial_transactions(file_path)
    assert isinstance(result, list)
    assert len(result) > 0

def test_financial_transactions_file_not_found():
    """Тест с отсутствующими транзакциями"""
    result = financial_transactions("non_existent_file.json")
    assert result == []

def test_financial_transactions_empty_json(tmp_path):
    """Тест с пустыми финансовыми транзакциями"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("")

    result = financial_transactions(empty_file)
    assert result == []

# --- get_transactions_amount_in_rub ---

@patch('src.utils.convert_to_rub')
def test_get_transactions_amount_in_rub(mock_get):
    """Тест с валютой в RUB"""
    rub_currency = {
        "operationAmount": {
            "amount": 500,
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = get_transactions_amount_in_rub(transaction=rub_currency)
    assert result == 500
    mock_get.assert_not_called()

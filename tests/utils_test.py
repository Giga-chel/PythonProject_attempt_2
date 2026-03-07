import os

from src.utils import financial_transactions

def test_financial_transactions_success():
    """Тест функции с финансовыми транзакциями на успех"""
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    result = financial_transactions(file_path)
    assert isinstance(result, list)
    assert len(result) > 0

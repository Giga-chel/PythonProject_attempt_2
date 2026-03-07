import os

from src.utils import financial_transactions

def test_financial_transactions_success():
    """Тест функции с финансовыми транзакциями на успех"""
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    result = financial_transactions(file_path)
    assert isinstance(result, list)
    assert len(result) > 0

def test_financial_transactions_file_not_found():
    result = financial_transactions("non_existent_file.json")
    assert result == []

def test_financial_transactions_empty_json(tmp_path):
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("")

    result = financial_transactions(empty_file)
    assert result == []

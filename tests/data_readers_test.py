import os
from unittest.mock import patch, mock_open

from src.data_readers import financial_transactions_csv, financial_transactions_xlsx

# --- financial_transactions_csv ---

csv_data = "id;amount;currency\n1;1000.0;RUB\n2;50.0;USD"

@patch("builtins.open", new_callable=mock_open, read_data=csv_data)
def test_financial_transactions_csv_success(mock_file):
    """Тест функции с чтением финансовых транзакций CSV-файла"""
    file_path = "data/transactions.csv"

    result = financial_transactions_csv(file_path)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]['id'] == '1'

    mock_file.assert_called_once_with("data/transactions.csv", encoding="utf-8")

@patch("builtins.open", side_effect=mock_open)
def test_financial_transactions_csv_not_found(mock_file):
    """Тест, если CSV файл не найден"""
    result = financial_transactions_csv("data/transactions.csv")
    assert result == []


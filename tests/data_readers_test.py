import os
import pandas as pd
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

# --- financial_transactions_xlsx ---

@patch("src.data_readers.pd.read_excel")
def test_financial_transactions_xlsx_success(mock_read_excel):
    """Тест функции с чтением финансовых транзакций XLSX-файла"""
    df_data = {"id": [10], "amount": [100], "currency": ["USD"]}
    mock_df = pd.DataFrame(df_data)
    mock_read_excel.return_value = mock_df

    file_path = "data/transactions_excel.xlsx"

    result = financial_transactions_xlsx(file_path)

    assert isinstance(result, list)
    assert result[0]['currency'] == 'USD'
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")

@patch("src.data_readers.pd.read_excel", side_effect=FileNotFoundError)
def test_financial_transactions_xlsx_not_found(mock_read_excel):
    """Тест, если XLSX файл не найден"""
    result = financial_transactions_xlsx("data/transactions_excel.xlsx")
    assert result == []
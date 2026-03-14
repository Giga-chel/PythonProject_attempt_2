import pandas as pd
import csv

def financial_transactions_csv(file_path: str) -> list:
    """Функция с CSV-данными о финансовых транзакциях"""
    try:
        with open(file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            data = list(csv_reader)
    except FileNotFoundError:
        data = []
    return data

def financial_transactions_xlsx(file_path: str) -> list:
    """Функция с XLSX-данными о финансовых транзакциях"""
    try:
        df = pd.read_excel(file_path)
        data = df.to_dict('records')
    except Exception:
        data = []
    return data

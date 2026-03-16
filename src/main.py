import json
import csv
import openpyxl



from src.services import process_bank_search, process_bank_operations
from src.data_readers import financial_transactions_csv, financial_transactions_xlsx
from src.utils import financial_transactions


def main():
    user_choice = input('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    if user_choice == '1':
        data = financial_transactions()
    elif user_choice == '2':
        data = financial_transactions_csv()
    elif user_choice == '3':
        data = financial_transactions_xlsx()
    else:
        print('''Кажется вы выбрали не существующий пункт. 
          Попробуйте выбрать из предложенных вариантов тот который вам больше подходит:
          1. Получить информацию о транзакциях из JSON-файла
          2. Получить информацию о транзакциях из CSV-файла
          3. Получить информацию о транзакциях из XLSX-файла''')
        return

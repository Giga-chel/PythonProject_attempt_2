import json
import csv
import openpyxl


from datetime import datetime
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
    valid_status = ['EXECUTED', 'PENDING', 'CANCELLED']
    while True:
        status_input = input('Выберите по каким статусам выбрать операции \nEXECUTED \nPENDING \nCANCELLED').upper()
        if status_input in valid_status:
            filtered_data = []
            for item in data:
                if item['status'] == status_input:
                    filtered_data.append(item)

            print(f'Операции отфильтрованы по статусу {status_input}')
            break
        else:
            print('''Информации по данной операции нет.''')

    sort_the_date = input('Сортировать операции по дате? Да/Нет')
    if sort_the_date.upper() == 'ДА':
        descending_or_ascending = input('Отсортировать по \n1.Возрастанию \n2.Убыванию')
        if descending_or_ascending == '1':
            filtered_data = sorted(filtered_data, key=lambda k: datetime.strptime(k['date'], '%d-%m-%Y'), reverse=False)
        elif descending_or_ascending == '2':
            filtered_data = sorted(filtered_data, key=lambda k: datetime.strptime(k['date'], '%d-%m-%Y'), reverse=True)

    sort_in_rub = input('Выводить транзакции только в рублях? Да/Нет')
    if sort_in_rub.upper() == 'ДА':
        filtered_data = sorted(filtered_data, key=lambda l: l['operationAmount']['currency']['code'] == 'RUB')

import os
from datetime import datetime

from src.data_readers import financial_transactions_csv, financial_transactions_xlsx
from src.services import process_bank_search
from src.utils import financial_transactions


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    path_json = os.path.join(project_root, 'data', 'operations.json')
    path_csv = os.path.join(project_root, 'data', 'transactions.csv')
    path_xlsx = os.path.join(project_root, 'data', 'transactions_excel.xlsx')

    user_choice = input("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")
    if user_choice == "1":
        data = financial_transactions(path_json)
    elif user_choice == "2":
        data = financial_transactions_csv(path_csv)
    elif user_choice == "3":
        data = financial_transactions_xlsx(path_xlsx)
    else:
        print("""Кажется вы выбрали не существующий пункт.
          Попробуйте выбрать из предложенных вариантов тот который вам больше подходит:
          1. Получить информацию о транзакциях из JSON-файла
          2. Получить информацию о транзакциях из CSV-файла
          3. Получить информацию о транзакциях из XLSX-файла\n""")
        return
    valid_status = ["EXECUTED", "PENDING", "CANCELLED"]
    while True:
        status_input = input("Выберите по каким статусам выбрать операции \nEXECUTED \nPENDING \nCANCELLED\n").upper()
        if status_input in valid_status:
            filtered_data = []
            for item in data:
                item_status = item.get("status", item.get("state", ""))
                if str(item_status).upper() == status_input:
                    filtered_data.append(item)

            print(f"Операции отфильтрованы по статусу {status_input}")
            break
        else:
            print("""Информации по данной операции нет.""")

    sort_the_date = input("Сортировать операции по дате? Да/Нет\n")
    if sort_the_date.upper() == "ДА":
        descending_or_ascending = input("Отсортировать по \n1.Возрастанию \n2.Убыванию\n")
        def parse_date(date_str):
            try:
                return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            except ValueError:
                try:
                    return datetime.strptime(date_str, "%d-%m-%Y")
                except ValueError:
                    return datetime.min

        if descending_or_ascending == "1":
            filtered_data = sorted(filtered_data, key=lambda k: parse_date(k["date"]), reverse=False)
        elif descending_or_ascending == "2":
            filtered_data = sorted(filtered_data, key=lambda k: parse_date(k["date"]), reverse=True)

    sort_in_rub = input("Выводить транзакции только в рублях? Да/Нет\n")
    if sort_in_rub.upper() == "ДА":
        rub_data = []
        for item in filtered_data:
            code = item.get("currency_code")
            if not code:
                code = item.get("operationAmount", {}).get("currency", {}).get("code")

            if code == "RUB":
                rub_data.append(item)
        filtered_data = rub_data

    sort_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if sort_description.upper() == "ДА":
        search_string = input("По какому слову ищем операцию?\n")
        filtered_data = process_bank_search(filtered_data, search_string)

    print("Распечатываю итоговый список транзакций...")

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}")
        for item in filtered_data:
            date = item.get("date", "")
            amount = item.get("amount")
            currency = item.get("currency_name")

            if amount is None:
                amount_info = item.get("operationAmount", {})
                amount = amount_info.get("amount", 0)
                currency = amount_info.get("currency", {}).get("name", "")

            who_send = item.get("from", "Неизвестно")
            who_receive = item.get("to", "Неизвестно")
            description = item.get("description", "")

            print(f"{date} {description}")
            print(f"Сумма: {amount} {currency}")
            print(f"{who_send} -> {who_receive}")
            print("")

if __name__ == '__main__':
    main()
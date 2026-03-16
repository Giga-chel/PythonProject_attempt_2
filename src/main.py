from datetime import datetime

from src.data_readers import financial_transactions_csv, financial_transactions_xlsx
from src.services import process_bank_search
from src.utils import financial_transactions


def main():
    user_choice = input("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
    if user_choice == "1":
        data = financial_transactions()
    elif user_choice == "2":
        data = financial_transactions_csv()
    elif user_choice == "3":
        data = financial_transactions_xlsx()
    else:
        print("""Кажется вы выбрали не существующий пункт.
          Попробуйте выбрать из предложенных вариантов тот который вам больше подходит:
          1. Получить информацию о транзакциях из JSON-файла
          2. Получить информацию о транзакциях из CSV-файла
          3. Получить информацию о транзакциях из XLSX-файла""")
        return
    valid_status = ["EXECUTED", "PENDING", "CANCELLED"]
    while True:
        status_input = input("Выберите по каким статусам выбрать операции \nEXECUTED \nPENDING \nCANCELLED").upper()
        if status_input in valid_status:
            filtered_data = []
            for item in data:
                if item["status"] == status_input:
                    filtered_data.append(item)

            print(f"Операции отфильтрованы по статусу {status_input}")
            break
        else:
            print("""Информации по данной операции нет.""")

    sort_the_date = input("Сортировать операции по дате? Да/Нет")
    if sort_the_date.upper() == "ДА":
        descending_or_ascending = input("Отсортировать по \n1.Возрастанию \n2.Убыванию")
        if descending_or_ascending == "1":
            filtered_data = sorted(
                filtered_data, key=lambda k: datetime.strptime(k["date"], "%d-%m-%Y"), reverse=False
            )
        elif descending_or_ascending == "2":
            filtered_data = sorted(filtered_data, key=lambda k: datetime.strptime(k["date"], "%d-%m-%Y"), reverse=True)

    sort_in_rub = input("Выводить транзакции только в рублях? Да/Нет")
    if sort_in_rub.upper() == "ДА":
        filtered_data = [item for item in filtered_data if item["operationAmount"]["currency"]["code"] == "RUB"]

    sort_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if sort_description.upper() == "ДА":
        search_string = input("По какому слову ищем операцию?")
        filtered_data = process_bank_search(filtered_data, search_string)

    print("Распечатываю итоговый список транзакций...")

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}")
        for item in filtered_data:
            date = item.get("date", "")
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

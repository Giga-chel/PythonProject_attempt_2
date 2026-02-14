def filter_by_state(operations: list[dict], state="EXECUTED") -> list[dict]:
    """Функция обработки данных"""
    data = []

    for operation in operations:
        if operation["state"] == state:
            data.append(operation)
    return data


def sort_by_date(data: list[dict], reverse=True) -> list[dict]:
    """Функция сортирующая дату, по убыванию"""
    date_and_time = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return date_and_time

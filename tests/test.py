from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card
from src.processing import filter_by_state, sort_by_date

print(get_mask_card_number(1234567890123456))

print(get_mask_account(12345678901234567890))
# print(get_mask_account(123456789567890))

if __name__ == "__main__":
    card_input = "Visa Platinum 7000792289606361"
    print(mask_account_card(card_input))

    account_input = "Счет 73654108430135874305"
    print(mask_account_card(account_input))

    maestro = "Maestro 7000792289606361"
    print(mask_account_card(maestro))

operations_list = [
    {"id": 1, "date": "2023-09-01T12:00:00", "state": "EXECUTED", "amount": 5000},
    {"id": 2, "date": "2023-10-15T14:30:00", "state": "CANCELED", "amount": 3000},
    {"id": 3, "date": "2023-08-20T09:15:00", "state": "EXECUTED", "amount": 10000},
    {"id": 4, "date": "2023-11-05T18:45:00", "state": "EXECUTED", "amount": 2000},
]

print("--- Результат фильтрации ---")
filtered_data = filter_by_state(operations_list)
print(filtered_data)

print("\n--- Результат сортировки ---")
sorted_data = sort_by_date(filtered_data)
print(sorted_data)
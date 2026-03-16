import pytest
from src.services import process_bank_search, process_bank_operations


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "description": "Перевод маме",
            "status": "EXECUTED",
            "operationAmount": {"amount": 100, "currency": {"code": "RUB"}}
        },
        {
            "id": 2,
            "description": "Покупка кофе",
            "status": "EXECUTED",
            "operationAmount": {"amount": 200, "currency": {"code": "RUB"}}
        },
        {
            "id": 3,
            "description": "Мама помогла с деньгами",
            "status": "CANCELED",
            "operationAmount": {"amount": 5000, "currency": {"code": "USD"}}
        },
        {
            "id": 4,
            "description": "Оплата интернета",
            "status": "PENDING",
            "operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}
        }
    ]


# --- process_bank_search ---

def test_search_found_without_register(transactions):
    """Тест функции на поиск без учета регистра"""
    result = process_bank_search(transactions, "МАМЕ")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_search_single_match(transactions):
    """Тест на поиск одного совпадения"""
    result = process_bank_search(transactions, "кофе")
    assert len(result) == 1
    assert result[0]["description"] == "Покупка кофе"


def test_search_no_match(transactions):
    """Тест на отсутствие совпадений, возвращается пустой список"""
    result = process_bank_search(transactions, "автомобиль")
    assert len(result) == 0
    assert result == []


def test_search_empty_data(transactions):
    """Тест с пустым списком транзакций"""
    result = process_bank_search([], "тест")
    assert result == []


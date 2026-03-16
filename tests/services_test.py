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


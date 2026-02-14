import pytest
from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    """Фикстура для модуля processing."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2015-01-15T13:54:29"},
        {"id": 2, "state": "CANCELED", "date": "2024-02-10T17:43:32"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-20T10:17:58"},
        {"id": 4, "state": "PENDING", "date": "2007-03-05T14:36:13"},
        {"id": 5, "state": "EXECUTED", "date": "2011-12-01T06:28:47"},
    ]

@pytest.fixture
def empty_transactions():
    """Фикстура с пустым списком."""
    return []

"""Тесты для модуля masks."""

@pytest.mark.parametrize("input_number, expected", [
        ("7000792289606361", "7000 79** **** 6361"),
        (1234567890123456, "1234 56** **** 3456"),
    ])
def test_mask_card_number(input_number, expected):
        """Тест маски карт (16 цифр)."""
        assert get_mask_card_number(input_number) == expected

@pytest.mark.parametrize("invalid_input", [
    "65784",
    "6878127452",
    "",
    "81645217446586541386494644654"
])
def test_mask_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной карт."""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)

@pytest.mark.parametrize("input_acc, expected", [
        ("73654108430135874305", "** 4305"),
        (10000000000000000000, "** 0000"),
    ])
def test_mask_account_card_number(input_acc, expected):
    """Тест маски корректных счетов(20 цифр)."""
    assert get_mask_account(input_acc) == expected

@pytest.mark.parametrize("invalid_input", ["34524", "", 52321])
def test_mask_account_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной счёта."""
    with pytest.raises(ValueError):
        get_mask_account(invalid_input)

"""Тесты для модуля widget"""

@pytest.mark.parametrize("input_str, expected", [
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
    ("Счет 73654108430135874305", "Счет ** 4305")
])
def test_mask_account_card_valid(input_str, expected):
    """Тест корректной маски карт и счетов."""
    assert mask_account_card(input_str) == expected

def test_mask_account_card_invalid_input():
    """Тест резист ошибок."""
    with pytest.raises(ValueError):
        mask_account_card("Visa 214")

    with pytest.raises(IndexError):
        mask_account_card("")

@pytest.mark.parametrize("input_date, expected", [
    ("2009-06-14T07:12:53.213425", "14.06.2009"),
    ("2015-11-25T16:37:21.734622", "25.11.2015")
])
def test_get_date_valid(input_date, expected):
    """Тест корректной даты."""
    assert get_date(input_date) == expected

@pytest.mark.parametrize("input_date", [
    "2016-09-25T08:53:22",
    "31.05.2019",
    "not a date"
])
def test_get_date_invalid(input_date):
    """Тест ошибок некорректного формата даты."""
    with pytest.raises(ValueError):
        get_date(input_date)

"""Тесты для модуля processing"""

def test_filter_by_state_default(sample_transactions):
    """Тест со значением state по умолчанию('EXECUTED')."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 3
    assert result[0]["state"] == "EXECUTED"

@pytest.mark.parametrize("state, expected", [
    ("CANCELED", 1),
    ("PENDING", 1),
    ("NOT_EXISTENT", 0),
])
def test_filter_by_state_various(sample_transactions, state, expected):
    """Тест с разными статусами."""
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected

def test_filter_by_state_empty(empty_transactions):
    """Тест с пустым списком."""
    assert filter_by_state(empty_transactions, "EXECUTED") == []

def test_sort_by_date_descending(sample_transactions):
    """Тест сортировки по убыванию."""
    result = sort_by_date(sample_transactions)
    ids = [t["id"] for t in result]
    assert ids == [2, 3, 1, 5, 4]

def test_sort_by_date_ascending(sample_transactions):
    """Тест сортировки по возрастанию."""
    result = sort_by_date(sample_transactions, reverse=False)
    ids = [t["id"] for t in result]
    assert ids == [4, 5, 1, 3, 2]

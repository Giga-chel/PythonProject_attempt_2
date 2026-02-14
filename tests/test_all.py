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
        assert mask_account_card(input_number) == expected

@pytest.mark.parametrize("invalid_input", [
    "65784", "6878127452", "", "81645217446586541386494644654"
])
def test_mask_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной карт."""
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)

@pytest.mark.parametrize("input_acc, expected", [
        ("73654108430135874305", "** 4305"),
        (10000000000000000000, "** 0000"),
    ])
def test_mask_account_card_number(input_acc, expected):
    """Тест маски корректных счетов(20 цифр)."""
    assert mask_account_card(input_acc) == expected

@pytest.mark.parametrize("invalid_input", ["34524", ""])
def test_mask_account_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной счёта."""
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)

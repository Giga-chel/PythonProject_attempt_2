import pytest

from src.widget import get_date, mask_account_card

"""Тесты для модуля widget"""

# --- mask_account_card ---


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет ** 4305"),
    ],
)
def test_mask_account_card_valid(input_str, expected):
    """Тест корректной маски карт и счетов."""
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_input():
    """Тест-резист ошибок."""
    with pytest.raises(ValueError):
        mask_account_card("Visa 214")

    with pytest.raises(IndexError):
        mask_account_card("")


# --- get_date ---


@pytest.mark.parametrize(
    "input_date, expected",
    [("2009-06-14T07:12:53.213425", "14.06.2009"), ("2015-11-25T16:37:21.734622", "25.11.2015")],
)
def test_get_date_valid(input_date, expected):
    """Тест корректной даты."""
    assert get_date(input_date) == expected


@pytest.mark.parametrize("input_date", ["2016-09-25T08:53:22", "31.05.2019", "not a date"])
def test_get_date_invalid(input_date):
    """Тест ошибок некорректного формата даты."""
    with pytest.raises(ValueError):
        get_date(input_date)

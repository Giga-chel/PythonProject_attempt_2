import pytest

from src.masks import get_mask_card_number, get_mask_account

"""Тесты для модуля masks."""

# --- get_mask_card_number ---

@pytest.mark.parametrize(
    "input_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (1234567890123456, "1234 56** **** 3456"),
    ],
)
def test_mask_card_number(input_number, expected):
    """Тест маски карт (16 цифр)."""
    assert get_mask_card_number(input_number) == expected


@pytest.mark.parametrize("invalid_input", ["65784", "6878127452", "", "81645217446586541386494644654"])
def test_mask_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной карт."""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)

# --- get_mask_account ---

@pytest.mark.parametrize(
    "input_acc, expected",
    [
        ("73654108430135874305", "** 4305"),
        (10000000000000000000, "** 0000"),
    ],
)
def test_mask_account_card_number(input_acc, expected):
    """Тест маски корректных счетов(20 цифр)."""
    assert get_mask_account(input_acc) == expected


@pytest.mark.parametrize("invalid_input", ["34524", "", 52321])
def test_mask_account_card_number_exception(invalid_input):
    """Проверка на ValueError с длиной счёта."""
    with pytest.raises(ValueError):
        get_mask_account(invalid_input)

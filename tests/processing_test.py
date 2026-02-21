import pytest

from src.processing import filter_by_state, sort_by_date

"""Тесты для модуля processing"""

# --- filter_by_state ---


def test_filter_by_state_default(sample_transactions):
    """Тест со значением state по умолчанию('EXECUTED')."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 3
    assert result[0]["state"] == "EXECUTED"


@pytest.mark.parametrize(
    "state, expected",
    [
        ("CANCELED", 1),
        ("PENDING", 1),
        ("NOT_EXISTENT", 0),
    ],
)
def test_filter_by_state_various(sample_transactions, state, expected):
    """Тест с разными статусами."""
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected


def test_filter_by_state_empty(empty_transactions):
    """Тест с пустым списком."""
    assert filter_by_state(empty_transactions, "EXECUTED") == []


# --- sort_by_date ---


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

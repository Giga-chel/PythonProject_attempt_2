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

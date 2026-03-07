import pytest
from src.external_api import convert_to_rub
from unittest.mock import patch

@patch('src.external_api.requests.get')
def test_convert_to_rub_success(mock_get):
    """Тест функции на успешную конвертацию в рубли"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 90.5}}
    result = convert_to_rub(100, "USD")
    assert result == 90.5 * 100
    assert mock_get.called

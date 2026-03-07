from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get):
    """Тест функции на успешную конвертацию в рубли"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.5}}
    result = convert_to_rub(100, "USD")
    assert result == 90.5 * 100
    assert mock_get.called


@patch("src.external_api.requests.get")
def test_convert_to_rub_fail(mock_get):
    """Тест функции на сбой"""
    mock_get.return_value.status_code = 500
    result = convert_to_rub(100, "USD")
    assert result == 0.0
    assert mock_get.called

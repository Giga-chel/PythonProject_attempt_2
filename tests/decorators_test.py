import pytest

from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def log_console(a, b):
        return a + b

    log_console(2, 3)
    captured = capsys.readouterr()
    assert "успешно" in captured.out

def test_log_console_error(capsys):
    @log()
    def log_console(a, b):
        raise Exception('Ошибка!')

    with pytest.raises(Exception):
        log_console(2, 4)

    captured = capsys.readouterr()
    assert "ошибкой" in captured.out

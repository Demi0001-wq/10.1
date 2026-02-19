import os
from typing import Any

from src.decorators import log


def test_log_console_success(capsys: Any) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_console_error(capsys: Any) -> None:
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success() -> None:
    filename = "test_log_success.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def multiply(x: int, y: int) -> int:
        return x * y

    assert multiply(2, 3) == 6
    with open(filename, "r") as f:
        content = f.read().strip()
    assert content == "multiply ok"
    os.remove(filename)


def test_log_file_error() -> None:
    filename = "test_log_error.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def fail_func() -> None:
        raise ValueError("Something went wrong")

    try:
        fail_func()
    except ValueError:
        pass

    with open(filename, "r") as f:
        content = f.read().strip()
    assert "fail_func error: ValueError. Inputs: (), {}" in content
    os.remove(filename)

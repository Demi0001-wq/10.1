import os
import pytest
from src.decorators import log


def test_log_console_success(capsys):
    """Test logging to console on successful execution."""
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"
    
    
def test_log_console_error(capsys):
    """Test logging to console on error."""
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path):
    """Test logging to a file on success."""
    log_file = tmp_path / "test.log"
    
    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    multiply(2, 3)
    
    assert log_file.exists()
    assert log_file.read_text().strip() == "multiply ok"


def test_log_file_error(tmp_path):
    """Test logging to a file on error."""
    log_file = tmp_path / "error.log"
    
    @log(filename=str(log_file))
    def fail():
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        fail()
    
    assert log_file.exists()
    content = log_file.read_text().strip()
    assert "fail error: ValueError. Inputs: (), {}" in content


def test_log_no_args(capsys):
    """Test decorator without parentheses if supported (though our implementation requires them)."""
    # Current implementation log() returns a decorator, so @log is not enough.
    # We must use @log() or @log(filename="...")
    pass

@log()
def sample_func():
    """Sample docstring."""
    return "done"


def test_log_wraps():
    """Test that decorator preserves function metadata."""
    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Sample docstring."
    assert "logs the execution" not in (sample_func.__doc__ or "")

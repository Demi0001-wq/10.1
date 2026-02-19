from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import get_transactions


def test_get_transactions_valid() -> None:
    mock_data = '[{"id": 1, "state": "EXECUTED"}]'
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = get_transactions("dummy.json")
            assert result == [{"id": 1, "state": "EXECUTED"}]


def test_get_transactions_not_found() -> None:
    with patch("os.path.exists", return_value=False):
        result = get_transactions("non_existent.json")
        assert result == []


def test_get_transactions_empty() -> None:
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data="")):
            result = get_transactions("empty.json")
            assert result == []


def test_get_transactions_not_list() -> None:
    mock_data = '{"id": 1}'
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = get_transactions("not_list.json")
            assert result == []


def test_get_transactions_invalid_json() -> None:
    mock_data = '[invalid json'
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = get_transactions("invalid.json")
            assert result == []

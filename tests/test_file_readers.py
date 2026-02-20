from unittest.mock import patch

import pandas as pd

from src.file_readers import read_csv
from src.file_readers import read_excel


def test_read_csv_success() -> None:
    mock_df = pd.DataFrame([{"id": 1, "state": "EXECUTED"}])
    with patch("pandas.read_csv", return_value=mock_df):
        result = read_csv("dummy.csv")
        assert result == [{"id": 1, "state": "EXECUTED"}]


def test_read_csv_failure() -> None:
    with patch("pandas.read_csv", side_effect=Exception("Error")):
        result = read_csv("invalid.csv")
        assert result == []


def test_read_excel_success() -> None:
    mock_df = pd.DataFrame([{"id": 2, "state": "PENDING"}])
    with patch("pandas.read_excel", return_value=mock_df):
        result = read_excel("dummy.xlsx")
        assert result == [{"id": 2, "state": "PENDING"}]


def test_read_excel_failure() -> None:
    with patch("pandas.read_excel", side_effect=Exception("Error")):
        result = read_excel("invalid.xlsx")
        assert result == []

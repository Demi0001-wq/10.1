import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize("data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837405946281", "Maestro 1596 83** **** 6281"),
    ("Account 12345678901234567890", "Account **7890"),
])
def test_mask_account_card(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-12-31T23:59:59", "31.12.2018"),
])
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


def test_mask_account_card_invalid() -> None:
    # Should handle empty input gracefully or as implemented
    assert mask_account_card("Visa 123") == "Visa **123"


def test_get_date_invalid() -> None:
    assert get_date("") == ""
    assert get_date("invalid-date") == ""

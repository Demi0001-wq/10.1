import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize("card, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("123456", "1234 56** **** 3456"),  # Non-standard length (123456 -> 1234 56** **** 3456 because of indices)
    ("", ""),  # Empty string
])
def test_get_mask_card_number(card: str, expected: str) -> None:
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("account, expected", [
    ("73654108430135874305", "**4305"),
    ("123456", "**3456"),
    ("123", "***"),  # Less than 4 digits
    ("", ""),
])
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected

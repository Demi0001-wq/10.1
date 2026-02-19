import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_currency() -> None:
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    for tx in usd_transactions:
        assert tx["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions() -> None:
    transactions = [
        {"description": "Transfer 1"},
        {"description": "Transfer 2"},
        {},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Transfer 1", "Transfer 2", ""]


def test_card_number_generator() -> None:
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(gen)


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []

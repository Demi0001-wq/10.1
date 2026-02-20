import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions_data():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transfer 1"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Transfer 2"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transfer 3"
        }
    ]

def test_filter_by_currency(transactions_data):
    usd_iter = filter_by_currency(transactions_data, "USD")
    assert next(usd_iter)["id"] == 1
    assert next(usd_iter)["id"] == 3
    with pytest.raises(StopIteration):
        next(usd_iter)

def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []

def test_transaction_descriptions(transactions_data):
    desc_iter = transaction_descriptions(transactions_data)
    assert next(desc_iter) == "Transfer 1"
    assert next(desc_iter) == "Transfer 2"
    assert next(desc_iter) == "Transfer 3"

@pytest.mark.parametrize("start, stop, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
])
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected

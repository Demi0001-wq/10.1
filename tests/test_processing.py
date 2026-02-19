import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(transaction_data: list[dict]) -> None:
    # Default (EXECUTED)
    result = filter_by_state(transaction_data)
    assert len(result) == 2
    for item in result:
        assert item['state'] == 'EXECUTED'

    # Specific (CANCELED)
    result_canceled = filter_by_state(transaction_data, 'CANCELED')
    assert len(result_canceled) == 2
    for item in result_canceled:
        assert item['state'] == 'CANCELED'

    # None matching
    assert filter_by_state(transaction_data, 'NON_EXISTENT') == []

    # Empty list
    assert filter_by_state([], 'EXECUTED') == []


@pytest.mark.parametrize("reverse, expected_first_date", [
    (True, '2019-07-03T18:35:29.512364'),
    (False, '2018-06-30T02:08:58.425572'),
])
def test_sort_by_date(transaction_data: list[dict], reverse: bool, expected_first_date: str) -> None:
    result = sort_by_date(transaction_data, reverse=reverse)
    assert result[0]['date'] == expected_first_date


def test_sort_by_date_same_dates() -> None:
    data = [
        {'id': 1, 'date': '2019-01-01T00:00:00'},
        {'id': 2, 'date': '2019-01-01T00:00:00'},
    ]
    result = sort_by_date(data)
    assert len(result) == 2


def test_sort_by_date_empty() -> None:
    assert sort_by_date([]) == []

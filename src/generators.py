from typing import Iterable, Iterator, List, Dict, Any

def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Filters a list of transactions by a given currency code.

    :param transactions: List of transaction dictionaries.
    :param currency_code: The currency code to filter by (e.g., 'USD').
    :return: An iterator yielding transactions matching the currency.
    """
    for transaction in transactions:
        amount_data = transaction.get("operationAmount", {})
        currency_data = amount_data.get("currency", {})
        if currency_data.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Generates descriptions for each transaction in turn.

    :param transactions: List of transaction dictionaries.
    :return: An iterator yielding transaction descriptions.
    """
    for transaction in transactions:
        yield transaction.get("description", "No description")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Generates bank card numbers in the format XXXX XXXX XXXX XXXX within a specified range.

    :param start: Starting number.
    :param stop: End number (inclusive).
    :return: An iterator yielding formatted card number strings.
    """
    for num in range(start, stop + 1):
        num_str = str(num).zfill(16)
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number

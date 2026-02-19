from typing import Generator
from typing import Iterable


def filter_by_currency(transactions: Iterable[dict], currency: str) -> Generator[dict, None, None]:
    """
    Returns an iterator that yields transactions with the specified currency.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Generator[str, None, None]:
    """
    Returns an iterator that yields descriptions for each transaction.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Generates card numbers in the specified range.
    Format: XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop + 1):
        num_str = str(number).zfill(16)
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted

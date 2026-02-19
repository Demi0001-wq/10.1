import re
from collections import Counter
from typing import Any


def filter_by_state(records: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Filter by state."""
    return [record for record in records if record.get("state") == state]


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """Sort by date."""
    return sorted(records, key=lambda x: x["date"], reverse=reverse)


def process_bank_search(data: list[dict[str, Any]], search_string: str) -> list[dict[str, Any]]:
    """
    Search for transactions by description using regex.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [
        item for item in data
        if item.get("description") and pattern.search(item["description"])
    ]


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """
    Count the number of transactions for each specified category.
    """
    descriptions = [
        item["description"] for item in data
        if item.get("description") in categories
    ]
    counts = Counter(descriptions)
    return {category: counts[category] for category in categories}

def filter_by_state(records: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Filter by state."""
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """Sort by date."""
    return sorted(records, key=lambda x: x['date'], reverse=reverse)

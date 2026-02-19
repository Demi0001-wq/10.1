from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info: str) -> str:
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет") or name.lower().startswith("account"):
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Format date."""
    if not date_string:
        return ""
    try:
        date_part = date_string.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except (ValueError, IndexError):
        return ""

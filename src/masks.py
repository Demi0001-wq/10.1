def get_mask_card_number(card_number: str) -> str:
    """Mask card number."""
    if not card_number:
        return ""
    masked = card_number[:6] + "*" * 6 + card_number[-4:]
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


def get_mask_account(account_number: str) -> str:
    """Mask account number."""
    if len(account_number) < 4:
        return "*" * len(account_number)
    return f"**{account_number[-4:]}"

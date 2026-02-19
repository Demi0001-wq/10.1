import logging
import os

# Configure logging
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join("logs", "masks.log"), mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_mask_card_number(card_number: str) -> str:
    """Mask card number."""
    logger.debug(f"Masking card number: {card_number}")
    if not card_number:
        logger.debug("Empty card number provided")
        return ""
    try:
        masked = card_number[:6] + "*" * 6 + card_number[-4:]
        result = f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}".strip()
        logger.debug(f"Successfully masked card number: {result}")
        return result
    except Exception as e:
        logger.error(f"Error masking card number: {e}")
        return ""


def get_mask_account(account_number: str) -> str:
    """Mask account number."""
    logger.debug(f"Masking account number: {account_number}")
    if len(account_number) < 4:
        logger.debug(f"Account number too short: {account_number}")
        return "*" * len(account_number)
    try:
        result = f"**{account_number[-4:]}"
        logger.debug(f"Successfully masked account number: {result}")
        return result
    except Exception as e:
        logger.error(f"Error masking account number: {e}")
        return ""

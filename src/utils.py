import json
import logging
import os
from typing import Any

# Configure logging
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join("logs", "utils.log"), mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_transactions(path: str) -> list[dict[str, Any]]:
    """
    Reads financial transaction data from a JSON file.
    Returns a list of dictionaries.
    If the file is not found, empty, or not a list, returns an empty list.
    """
    logger.debug(f"Reading transactions from: {path}")
    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Successfully read {len(data)} transactions")
                return data
            logger.error(f"Data is not a list in file: {path}")
            return []
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error reading file {path}: {e}")
        return []

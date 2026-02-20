from typing import Any
from typing import cast

import pandas as pd


def read_csv(path: str) -> list[dict[str, Any]]:
    """
    Reads financial transactions from a CSV file.
    Returns a list of dictionaries.
    """
    try:
        df = pd.read_csv(path, sep=None, engine="python")
        return cast(list[dict[str, Any]], df.to_dict(orient="records"))
    except Exception:
        return []


def read_excel(path: str) -> list[dict[str, Any]]:
    """
    Reads financial transactions from an Excel file.
    Returns a list of dictionaries.
    """
    try:
        df = pd.read_excel(path)
        return cast(list[dict[str, Any]], df.to_dict(orient="records"))
    except Exception:
        return []

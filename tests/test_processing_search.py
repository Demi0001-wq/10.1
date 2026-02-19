from src.processing import process_bank_operations
from src.processing import process_bank_search


def test_process_bank_search_found() -> None:
    data: list[dict] = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]
    result = process_bank_search(data, "Перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_process_bank_search_regex() -> None:
    data: list[dict] = [
        {"description": "Visa Platinum 1234"},
        {"description": "Mastercard 5678"},
    ]
    result = process_bank_search(data, r"Visa\s+Platinum")
    assert len(result) == 1
    assert result[0]["description"] == "Visa Platinum 1234"


def test_process_bank_search_empty() -> None:
    data: list[dict] = []
    assert process_bank_search(data, "test") == []


def test_process_bank_operations() -> None:
    data: list[dict] = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Внешний перевод"},
    ]
    categories = ["Перевод организации", "Открытие вклада", "Внешний перевод", "Неизвестно"]
    result = process_bank_operations(data, categories)
    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Внешний перевод": 1,
        "Неизвестно": 0,
    }

import pytest
from src.category import Category

@pytest.fixture(autouse=True)
def reset_counts():
    """Reset class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0

import pytest

from src.category import Category
from src.product import Product





def test_category_init() -> None:
    """Test category initialization and counters."""
    product1 = Product("Samsung Galaxy S23 Ultra", "200MP", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    
    category = Category("Смартфоны", "Description", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Description"
    assert "Samsung Galaxy S23 Ultra" in category.products
    assert "Iphone 15" in category.products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories() -> None:
    """Test counting multiple categories and products."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    c1 = Category("C1", "D1", [p1, p2])

    p3 = Product("P3", "D3", 300.0, 30)
    c2 = Category("C2", "D2", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_average_price() -> None:
    """Test average price calculation in category."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    category = Category("C", "D", [p1, p2])
    assert category.average_price() == 150.0


def test_category_average_price_empty() -> None:
    """Test average price for empty category."""
    category = Category("Empty", "D", [])
    assert category.average_price() == 0.0

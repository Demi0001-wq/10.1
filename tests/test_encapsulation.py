from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Reset the class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_price_setter_decrease_confirm(capsys) -> None:
    """Test price setter with decrease confirmation (Yes)."""
    product = Product("Test", "Desc", 100.0, 10)
    
    with patch("builtins.input", return_value="y"):
        product.price = 80.0
    
    assert product.price == 80.0


def test_product_price_setter_decrease_cancel(capsys) -> None:
    """Test price setter with decrease confirmation (No)."""
    product = Product("Test", "Desc", 100.0, 10)
    
    with patch("builtins.input", return_value="n"):
        product.price = 80.0
    
    assert product.price == 100.0


def test_product_price_setter_invalid(capsys) -> None:
    """Test price setter with invalid values."""
    product = Product("Test", "Desc", 100.0, 10)
    
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_new_product_duplicate() -> None:
    """Test duplicate detection and merging in new_product."""
    p1 = Product("Samsung", "Old", 100.0, 5)
    existing = [p1]
    
    # Add same product with higher price and more quantity
    data = {"name": "Samsung", "description": "New", "price": 150.0, "quantity": 10}
    result = Product.new_product(data, existing)
    
    assert result == p1
    assert p1.price == 150.0
    assert p1.quantity == 15


def test_category_products_getter() -> None:
    """Test formatted string output of products getter."""
    p1 = Product("Product A", "D1", 100.0, 10)
    p2 = Product("Product B", "D2", 200.0, 20)
    category = Category("C1", "D1", [p1, p2])
    
    # Each product line should end with a newline
    expected = (
        "Product A, 100.0 руб. Остаток: 10 шт.\n"
        "Product B, 200.0 руб. Остаток: 20 шт.\n"
    )
    assert category.products == expected


def test_private_attributes_mangling() -> None:
    """Verify that private attributes are correctly mangled and not accessible directly."""
    product = Product("P", "D", 100.0, 10)
    category = Category("C", "D", [product])
    
    # Checking for name mangling
    with pytest.raises(AttributeError):
        _ = product.__price
        
    with pytest.raises(AttributeError):
        _ = category.__products
        
    # Verify they exist via name mangling
    assert hasattr(product, "_Product__price")
    assert hasattr(category, "_Category__products")


def test_product_price_setter_with_input(capsys) -> None:
    """Test price setter logic including lower price confirmation."""
    product = Product("Test", "Desc", 100.0, 10)
    
    # Setting higher price - no input needed
    product.price = 150.0
    assert product.price == 150.0
    
    # Setting lower price - confirmation 'y'
    with patch("builtins.input", return_value="y"):
        product.price = 120.0
    assert product.price == 120.0
    
    # Setting lower price - confirmation 'n'
    with patch("builtins.input", return_value="n"):
        product.price = 80.0
    assert product.price == 120.0

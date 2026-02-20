from unittest.mock import patch
import pytest
from src.category import Category
from src.product import Product

@pytest.fixture(autouse=True)
def reset_category_counts():
    """Reset the class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0

def test_category_private_products():
    """Task 1: Verify Category has private products attribute."""
    cat = Category("Electronics", "Gadgets")
    assert hasattr(cat, "_Category__products")
    # Verify products property is used for string output
    assert isinstance(cat.products, str)

def test_category_add_product():
    """Task 1: Verify add_product logic and counters."""
    cat = Category("Electronics", "Gadgets")
    p1 = Product("Phone", "Smart", 500.0, 10)
    cat.add_product(p1)
    
    assert Category.product_count == 1
    assert p1 in cat._Category__products

def test_category_products_getter_format():
    """Task 2: Verify products property strictly follows the requested template."""
    p1 = Product("Samsung Galaxy S23 Ultra", "200MP", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB", 210000.0, 8)
    cat = Category("Смартфоны", "Description", [p1, p2])
    
    # Template: "Название продукта, X руб. Остаток: X шт.\n"
    expected = (
        "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000 руб. Остаток: 8 шт.\n"
    )
    assert cat.products == expected

def test_product_new_product_merging():
    """Task 3: Verify new_product creates objects and merges duplicates."""
    p1 = Product("Laptop", "Silver", 1000.0, 5)
    existing = [p1]
    
    # Same name, higher price, more quantity
    data = {"name": "Laptop", "description": "Black", "price": 1200.0, "quantity": 10}
    p_result = Product.new_product(data, existing)
    
    assert p_result == p1
    assert p1.quantity == 15
    assert p1.price == 1200.0

def test_product_price_setter_validation(capsys):
    """Task 4: Verify price setter correctly validates values."""
    p = Product("Test", "Desc", 100.0, 10)
    
    # Invalid price
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 100.0
    
    # Lower price with confirmation 'y'
    with patch("builtins.input", return_value="y"):
        p.price = 80.0
    assert p.price == 80.0
    
    # Lower price with cancellation 'n'
    with patch("builtins.input", return_value="n"):
        p.price = 50.0
    assert p.price == 80.0
    
    # Higher price - no confirmation needed
    p.price = 150.0
    assert p.price == 150.0

def test_total_counters():
    """Test overall counters for categories and products."""
    c1 = Category("C1", "D1", [Product("P1", "D", 10, 1)])
    c2 = Category("C2", "D2", [Product("P2", "D", 20, 2), Product("P3", "D", 30, 3)])
    
    assert Category.category_count == 2
    assert Category.product_count == 3

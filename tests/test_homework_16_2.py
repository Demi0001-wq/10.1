import pytest

from src.base_category import BaseCategory
from src.base_product import BaseProduct
from src.category import Category
from src.order import Order
from src.product import Product, Smartphone


@pytest.fixture(autouse=True)
def reset_counts():
    """Reset class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0


def test_base_product_cannot_instantiate():
    with pytest.raises(TypeError):
        BaseProduct() # type: ignore


def test_base_category_cannot_instantiate():
    with pytest.raises(TypeError):
        BaseCategory() # type: ignore


def test_print_mixin_logging(capsys):
    Product("Test Product", "Testing Mixin", 10.0, 5)
    captured = capsys.readouterr()
    assert "Product('Test Product', 'Testing Mixin', 10.0, 5)" in captured.out


def test_smartphone_logging(capsys):
    Smartphone("S", "D", 100.0, 1, 99.9, "M", 128, "Red")
    captured = capsys.readouterr()
    assert "Smartphone('S', 'D', 100.0, 1, 99.9, 'M', 128, 'Red')" in captured.out


def test_order_creation():
    p = Product("P", "D", 10.0, 100)
    o = Order(p, 5)
    assert o.product == p
    assert o.quantity == 5
    assert o.total_price == 50.0
    assert o.products == "P (x5)"


def test_order_validation():
    with pytest.raises(TypeError):
        Order("Not a product", 1) # type: ignore


def test_category_and_order_interfaces():
    p = Product("P", "D", 1.0, 1)
    o = Order(p, 1)
    c = Category("C", "D", [p])
    
    # Both should be instances of the BaseCategory interface
    assert isinstance(o, BaseCategory)
    assert isinstance(c, BaseCategory)

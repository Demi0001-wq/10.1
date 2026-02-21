import pytest

from src.base_category import BaseCategory
from src.category import Category
from src.order import Order
from src.product import Product





def test_order_init() -> None:
    p = Product("P", "D", 100.0, 10)
    o = Order(p, 2)
    assert o.product == p
    assert o.quantity == 2
    assert o.total_price == 200.0


def test_order_validation() -> None:
    with pytest.raises(TypeError):
        Order("Not a product", 1)  # type: ignore


def test_base_category_inheritance() -> None:
    # Verify that Category and Order both implement the BaseCategory interface
    p = Product("P", "D", 100.0, 10)
    cat = Category("C", "D", [p])
    o = Order(p, 1)
    
    assert isinstance(cat, BaseCategory)
    assert isinstance(o, BaseCategory)


def test_order_products_repr() -> None:
    p = Product("P", "D", 100.0, 10)
    o = Order(p, 5)
    assert o.products == "P (x5)"


def test_order_str() -> None:
    p = Product("P", "D", 100.0, 10)
    o = Order(p, 1)
    assert "Order: P" in str(o)
    assert "Total: 100.0" in str(o)

import pytest

from src.base_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


def test_base_product_instantiation() -> None:
    """Ensure BaseProduct cannot be instantiated directly."""
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore


def test_print_mixin_logic(capsys) -> None:
    """Verify that PrintMixin prints info during initialization."""
    Product("Test", "Desc", 10.0, 1)
    captured = capsys.readouterr()
    assert "Product('Test', 'Desc', 10.0, 1)" in captured.out


def test_smartphone_print_mixin(capsys) -> None:
    """Verify that Smartphone uses PrintMixin from Product."""
    Smartphone("S1", "D", 100.0, 1, 90.0, "M", 64, "Black")
    captured = capsys.readouterr()
    assert "Smartphone('S1', 'D', 100.0, 1, 90.0, 'M', 64, 'Black')" in captured.out


def test_product_str() -> None:
    """Verify __str__ works as expected."""
    p = Product("P", "D", 10.0, 5)
    assert str(p) == "P, 10.0 руб. Остаток: 5 шт."

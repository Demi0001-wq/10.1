import pytest

from src.category import Category
from src.exceptions import QuantityError
from src.product import Product





def test_custom_quantity_error_raised_on_init():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("P", "D", 100.0, 0)


def test_category_add_product_notifications(capsys):
    p = Product("P", "D", 100.0, 5)
    c = Category("C", "D")
    
    # Success addition
    c.add_product(p)
    captured = capsys.readouterr()
    assert "Товар успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_category_add_product_error_notifications(capsys):
    c = Category("C", "D")
    
    # Invalid addition
    with pytest.raises(TypeError):
        c.add_product("Not Product") # type: ignore
        
    captured = capsys.readouterr()
    assert "Ошибка при добавлении товара" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_average_price_calculation():
    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 1)
    c = Category("C", "D", [p1, p2])
    assert c.average_price() == 15.0


def test_average_price_empty():
    c = Category("Empty", "D", [])
    assert c.average_price() == 0.0

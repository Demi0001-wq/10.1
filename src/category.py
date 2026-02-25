from src.base_category import BaseCategory
from src.exceptions import QuantityError
from src.product import Product


class Category(BaseCategory):
    """Class representing a product category in the ecommerce project."""
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Adds a product to the category and validates its type and quantity."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to Category")
        
        try:
            if product.quantity == 0:
                raise QuantityError("Товар с нулевым количеством не может быть добавлен")
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        except QuantityError as e:
            print(f"Ошибка: {e}")
            raise e
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self):
        """Calculates the average price of all products in the category."""
        try:
            total_price = sum(p.price for p in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def get_products(self):
        """Returns the list of products (for iterator)."""
        return self.__products

    @property
    def products(self) -> str:
        """Returns a string representation of all products in the category."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self) -> str:
        """Returns string representation with product quantity."""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        return f"Category('{self.name}', '{self.description}', products={len(self.__products)})"

from src.base_category import BaseCategory
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
        self.__products = []
        if products:
            for product in products:
                try:
                    self.add_product(product)
                except (TypeError, Exception):
                    continue
        Category.category_count += 1

    def add_product(self, product):
        """Adds a product to the category and validates its type and quantity."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Only Product instances can be added to Category")
            
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        except TypeError as e:
            print(f"Ошибка при добавлении товара: {e}")
            raise e
        except Exception as e:
            print(f"Ошибка при добавлении товара: {e}")
            raise e
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Returns a string representation of all products in the category."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def middle_price(self):
        """Calculates the average price of all products in the category."""
        try:
            total_price = sum(p.price for p in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    def get_products(self):
        """Returns the list of products."""
        return self.__products

    def __str__(self) -> str:
        """Returns string representation with product quantity."""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        return f"Category('{self.name}', '{self.description}', products={len(self.__products)})"

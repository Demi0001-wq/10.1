from typing import Optional

from src.base_category import BaseCategory
from src.exceptions import QuantityError
from src.product import Product


class Category(BaseCategory):
    """Class representing a category of products."""
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        """
        Initialize a category.
        :param name: Name of the category
        :param description: Description of the category
        :param products: Initial list of products
        """
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for prod in products:
                # Use add_product to maintain tracking and notifications
                try:
                    self.add_product(prod)
                except QuantityError:
                    # During bulk init, we might log or skip invalid products
                    pass

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the category with type validation and notifications.
        Uses try/except/else/finally for robust event handling.
        """
        try:
            if not isinstance(product, Product):
                raise TypeError("Only products or their subclasses can be added to a category.")
            
            if product.quantity == 0:
                raise QuantityError("Товар с нулевым количеством не может быть добавлен")
            
            self.__products.append(product)
            Category.product_count += 1
            
        except (TypeError, QuantityError) as e:
            # Re-raise or handle as needed. Per requirement: "The exception should be raised"
            print(f"Ошибка при добавлении товара: {e}")
            raise
        else:
            # Per requirement: "display a message stating that the product has been added"
            print("Товар успешно добавлен")
        finally:
            # Per requirement: "display a message stating that the product addition has been completed"
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Getter for localized representation of products."""
        return "\n".join([str(p) for p in self.__products])

    def middle_price(self) -> float:
        """Calculates the average price of all products in the category."""
        try:
            total_price = sum(p.price for p in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        """String representation of the category."""
        # Total quantity across all products in this category
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

from typing import Optional

from src.base_category import BaseCategory
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
                self.add_product(prod)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Adds a product to the category with type validation."""
        if not isinstance(product, Product):
            raise TypeError("Only products or their subclasses can be added to a category.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Getter for localized representation of products."""
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def __str__(self) -> str:
        """String representation of the category."""
        # Total quantity across all products in this category
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

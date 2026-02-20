from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    """
    Class representing an order containing one type of product.
    Implements the BaseCategory interface.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("Order can only contain Product instances.")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        """String representation of the order."""
        return f"Order: {self.product.name} x {self.quantity}, Total: {self.total_price} руб."

    @property
    def products(self) -> str:
        """Returns the product description in the order."""
        return f"{self.product.name} (x{self.quantity})"

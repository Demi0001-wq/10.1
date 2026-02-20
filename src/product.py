from typing import Any, Optional


class Product:
    """Class representing a product in the store."""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Initialize a product.
        :param name: Name of the product
        :param description: Description of the product
        :param price: Product price (float)
        :param quantity: Quantity in stock (int)
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        String representation of the product.
        Format: "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """
        Magic method for adding two products.
        Returns the sum of (price * quantity) for both products.
        """
        if not isinstance(other, Product):
            raise TypeError("Can only add two Product objects.")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, data: dict[str, Any], existing_products: Optional[list["Product"]] = None) -> "Product":
        """
        Class method to create or update a Product instance from a dictionary.
        If a product with the same name exists in existing_products, it updates it.
        """
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    # Update found product
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Getter for the price attribute."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Setter for the price attribute with validation and manual confirmation."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirm = input("Цена понижается. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
        else:
            self.__price = value

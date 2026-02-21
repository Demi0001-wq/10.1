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
        p_price = int(self.price) if self.price == int(self.price) else self.price
        return f"{self.name}, {p_price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, data: dict[str, Any], existing_products: Optional[list["Product"]] = None) -> "Product":
        """
        Class method to create or update a Product instance from a dictionary.
        Task 3: If product exists, merges quantities and takes higher price.
        """
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Getter for the private price attribute."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Setter for the price attribute with validation and confirmation.
        Task 4: Checks for positive value and confirms price decrease.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirm = input("Цена понижается. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
        else:
            self.__price = value

class Product:
    """Class representing a product in the store."""
    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity

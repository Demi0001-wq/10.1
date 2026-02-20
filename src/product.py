class Product:
    """Class representing a product in the ecommerce project."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"

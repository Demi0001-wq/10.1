from src.base_product import BaseProduct
from src.exceptions import QuantityError
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Class representing a product in the ecommerce project."""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise QuantityError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None):
        """Creates a new product or updates an existing one."""
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        quantity = data.get("quantity")

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
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        
        if value < self.__price:
            confirm = input("Цена понижается. Вы уверены? (y/n): ")
            if confirm.lower() != "y":
                return
        
        self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Cannot add products of different classes")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Class representing a smartphone."""
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"


class LawnGrass(Product):
    """Class representing lawn grass."""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country}', '{self.germination_period}', '{self.color}')"

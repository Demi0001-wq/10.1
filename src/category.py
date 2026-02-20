from src.product import Product


class Category:
    """Class representing a category of products."""
    name: str
    description: str
    __products: list[Product]

    # Class attributes to track total counts
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Initialize a category.
        :param name: Category name
        :param description: Category description
        :param products: Initial list of Product objects
        """
        self.name = name
        self.description = description
        self.__products = []

        # Update category count
        Category.category_count += 1
        
        # Add products via the add_product method
        for product in products:
            self.add_product(product)

    def __str__(self) -> str:
        """
        String representation of the category.
        Format: "Название категории, количество продуктов: X шт."
        Where X is the total quantity of all goods in the warehouse.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """
        Add a product to the category and increment the class product counter.
        Only Product or its descendants can be added.
        """
        if not isinstance(product, Product):
            raise TypeError("Only products or their subclasses can be added to a category.")
        self.__products.append(product)
        Category.product_count += 1

    def get_products(self) -> list[Product]:
        """Returns the list of products."""
        return self.__products

    @property
    def products(self) -> str:
        """
        Getter that returns a string representation of all products in the category.
        Uses the Product.__str__ implementation.
        """
        result = [str(p) for p in self.__products]
        return "\n".join(result) + "\n" if result else ""

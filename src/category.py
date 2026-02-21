from src.product import Product


class Category:
    """Class representing a category of products."""
    name: str
    description: str
    products: list[Product]

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
        self.products = products

        # Update class-level counters
        Category.category_count += 1
        Category.product_count += len(products)

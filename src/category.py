class Category:
    """Class representing a product category in the ecommerce project."""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product):
        """Adds a product to the category."""
        self.products.append(product)
        Category.product_count += 1

    def __repr__(self):
        return f"Category({self.name}, {self.description}, products={len(self.products)})"

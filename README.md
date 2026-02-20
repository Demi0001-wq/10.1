# Skystore E-commerce Project

<<<<<<< Updated upstream
This project implements the foundational logic for an e-commerce platform using Object-Oriented Programming (OOP) principles in Python.

## Features

- Product Management: Track name, description, price, and quantity.
- Category Management: Group products and track global category/product statistics.
- Encapsulation: Private attributes for sensitive data like price and product lists.
- Data Integrity: Price validation with interactive confirmation for price drops.
- JSON Loading: Ability to deserialize project data from a `products.json` file.
- Smart Factory: Automated duplicate detection and merging in the `Product` class.
- Inheritance: Specialized Smartphone and LawnGrass classes with specific attributes.
- Type Safety: Addition is restricted to objects of the same class; Categories only accept Product instances.
=======
Foundational core for an e-commerce platform using Object-Oriented Programming (OOP) in Python.

## Description
This project implements the basic structure of an e-commerce system with `Product` and `Category` classes. It allows for tracking products, categories, and inventory statistics. Developed as part of the Skypro Python course (Lesson 14.1).

## Features
- **Product Management**: Store details like name, description, price, and quantity.
- **Category Management**: Group products and descriptions.
- **Automated Statistics**: 
  - `Category.category_count`: Tracks the total number of unique categories.
  - `Category.product_count`: Tracks the total number of unique products across all categories.
>>>>>>> Stashed changes

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Demi0001-wq/10.1.git
   ```
2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r pyproject.toml  # or use poetry install
   ```

## Usage Example

```python
from src.product import Product
from src.category import Category

# Create products
p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)
p2 = Product("Iphone 15", "512GB, Gray", 210000.0, 8)

# Create category
cat = Category("Smartphones", "Modern mobile devices", [p1, p2])

print(f"Total categories: {Category.category_count}")
print(f"Total products: {Category.product_count}")
```

## Testing
<<<<<<< Updated upstream

To run the unit tests and check coverage:
=======
Unit tests are implemented to verify class logic. Run them using:
>>>>>>> Stashed changes
```bash
poetry run pytest --cov=src
```
<<<<<<< Updated upstream

### Quality Checks
The project adheres to strict quality standards:
- Linting: flake8
- Type Checking: mypy
- Import Sorting: isort
=======
>>>>>>> Stashed changes

# Ecommerce Core Classes

A Python project implementing core logic for an e-commerce platform, including product and category management.

## Features

- **Product Management**: Define products with names, descriptions, prices, and quantities.
- **Category Management**: Group products into categories and track total counts of categories and products across the system.
- **Data Loading**: Utility to load category and product data from JSON files.

## Project Structure

- `src/`: Source code directory.
  - `product.py`: Contains the `Product` class.
  - `category.py`: Contains the `Category` class.
  - `utils.py`: Utility functions (e.g., `load_data`).
- `tests/`: Unit tests for the core classes and utilities.
- `main.py`: Entry point for basic demonstration or testing.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. Clone the repository and navigate to the project root.
2. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

Basic usage example:

```python
from src.product import Product
from src.category import Category

# Create products
p1 = Product("Samsung Galaxy S23 Ultra", "200MP camera", 180000.0, 5)
p2 = Product("Iphone 15", "512GB", 210000.0, 8)

# Create category
category = Category("Smartphones", "Modern mobile devices", [p1, p2])

print(f"Category: {category.name}")
print(f"Total Categories: {Category.category_count}")
print(f"Total Products: {Category.product_count}")
```

## Testing

Run tests using `pytest`:

```bash
pytest
```

To run with coverage report:

```bash
pytest --cov=src
```

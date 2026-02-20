# E-commerce Core Project

This project implements the foundational logic for an e-commerce platform using Object-Oriented Programming (OOP) principles in Python, featuring Product and Category classes. Developed as part of Lesson 14.1.

## Features

- Product Management: Track name, description, price, and quantity.
- Category Management: Group products and track global category and product statistics.
- Encapsulation: Use class attributes to track counts of categories and products.
- Serialization: Foundation for loading and saving e-commerce data.

## Installation

This project uses Poetry for dependency management.

1. Ensure you have Python 3.11 or higher installed.
2. Install Poetry:
   ```bash
   pip install poetry
   ```
3. Navigate to the project directory:
   ```bash
   cd 10.1
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

To use the classes in your script:

```python
from src.category import Category
from src.product import Product

product1 = Product("Smartphone", "High-end smartphone", 70000.0, 10)
category = Category("Electronics", "Category for electronics", [product1])
print(category)
```

## Testing

This project uses pytest for unit testing.

### Running Tests
To run all tests:
```bash
pytest
```

### Coverage Report
To generate a coverage report:
```bash
pytest --cov=src --cov-report=term-missing
```

The project maintains a high test coverage for all core logic.

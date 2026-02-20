# E-commerce Core Project

This project implements the foundational logic for an e-commerce platform using Object-Oriented Programming (OOP) principles in Python, featuring Product and Category classes. Developed as part of Lesson 14.1.

## Features

- Product Management: Track name, description, price, and quantity.
- Category Management: Group products and track global category/product statistics.
- Encapsulation: Private attributes for sensitive data like price and product lists.
- Data Integrity: Price validation and quantity management.
- JSON Loading: Ability to deserialize project data from a products.json file.

## Installation

1. Ensure you have Python 3.11+ installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Demi0001-wq/10.1.git
   ```
3. Navigate to the project directory:
   ```bash
   cd 10.1
   ```
4. Setup virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
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

This project uses pytest for unit testing.

### Running Tests
To run all tests:
```bash
pytest
```

### Coverage Report
To generate a coverage report:
```bash
pytest --cov=src
```

## Code Quality
The project follows PEP 8 standards and uses the following tools:
- Flake8: Linting
- Mypy: Type checking
- Isort: Import sorting

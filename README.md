# E-commerce Core Project

This project implements the foundational logic for an e-commerce platform using Object-Oriented Programming (OOP) principles in Python, featuring `Product` and `Category` classes.

## Features

- **Product Management**: Track name, description, price, and quantity.
- **Category Management**: Group products and track global category/product statistics.
- **Encapsulation**: Private attributes for sensitive data like price and product lists.
- **Data Integrity**: Price validation with interactive confirmation for price drops.
- **JSON Loading**: Ability to deserialize project data from a `products.json` file.
- **Smart Factory**: Automated duplicate detection and merging in the `Product` class.
- **Inheritance**: Specialized Smartphone and LawnGrass classes with specific attributes.
- **Type Safety**: Addition is restricted to objects of the same class; Categories only accept Product instances.
- **Abstraction**: Abstract Base Classes (ABCs) for Products and Categories ensure consistent interfaces.
- **Mixins**: Automatic object creation logging with `PrintMixin`.

## Installation

This project uses Poetry for dependency management.

1. Ensure you have Python 3.11+ installed.
2. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```
3. Navigate to the project directory:
   ```bash
   cd ecommerce
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

To run the demonstration script:
```bash
poetry run python main.py
```

## Testing

This project uses `pytest` for unit testing. The test suite covers masks, widgets, processing logic, and decorators.

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
The project maintains a test coverage of >80%. An HTML coverage report is available in the `htmlcov/` directory.

### Code Quality
The project follows PEP 8 standards and uses the following tools:
- **Flake8**: Linting
- **Mypy**: Type checking
- **Isort**: Import sorting


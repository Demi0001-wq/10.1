Banking Operations Widget

Banking utility for masking data, processing transactions, and logging.

## Features
- Masking card and account numbers
- Filtering and sorting transactions
- Iterative processing with generators
- Automated function logging
- CSV and Excel file reading support
- Regular expression search

## How to Run

### 1. Install Dependencies
```bash
pip install pandas openpyxl requests python-dotenv pytest pytest-cov
```

### 2. Set Up API Key
Create `.env` file and add `API_KEY=your_key`

## Usage

To run the demonstration script:
```bash
python main.py
```

## Generators Module

This module provides tools for efficient processing of large transaction datasets.

### `filter_by_currency`
Returns an iterator that yields transactions matching a specific currency code.
```python
usd_transactions = filter_by_currency(transactions, "USD")
```

### `transaction_descriptions`
Generates descriptions for each transaction in a list.
```python
descriptions = transaction_descriptions(transactions)
```

### `card_number_generator`
Generates formatted 16-digit card numbers in a given range.
```python
for card in card_number_generator(1, 10):
    print(card)
```

## Testing

This project uses `pytest` for unit testing. To run all tests and check coverage:
```bash
pytest --cov=src --cov-report=term-missing
```

The project maintains a test coverage of >80%. An HTML coverage report is available in the `htmlcov/` directory.

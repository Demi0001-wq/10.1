# Banking Operations Widget

A tool for masking sensitive data and processing transaction records.

## Features
- Mask card and account numbers
- Format transaction dates
- Filter and sort transaction lists
- **Generators** for efficient data processing

## Generators Module
The `src/generators.py` module provides tools for working with large volumes of transaction data:

### `filter_by_currency`
Returns an iterator of transactions matching a specific currency code (e.g., "USD").
```python
usd_transactions = filter_by_currency(transactions, "USD")
for tx in usd_transactions:
    print(tx)
```

### `transaction_descriptions`
Yields descriptions for each transaction in sequence.
```python
descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
```

### `card_number_generator`
Generates bank card numbers in `XXXX XXXX XXXX XXXX` format within a given range.
```python
for card in card_number_generator(1, 5):
    print(card)
```

## Testing
Run tests with `pytest`:
```bash
pytest --cov=src --cov-report=term-missing
```
Achieve 80%+ coverage across all modules.

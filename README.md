# Banking Operations Widget

Banking utility for masking data, processing transaction records, and automated logging.

## Features
- **Masking**: Card and account numbers.
- **Processing**: Filtering and sorting transactions.
- **Generators**: Efficient iterative processing.
- **Decorators**: Automated function logging.

## Generators Module
The `src/generators.py` module provides tools for working with large volumes of transaction data:
- `filter_by_currency`: Filters transactions by currency code.
- `transaction_descriptions`: Yields descriptions for each transaction.
- `card_number_generator`: Generates bank card numbers in `XXXX XXXX XXXX XXXX` format.

## Decorators Module
The `src/decorators.py` module provides the `@log` decorator:
- Logs function name and result on success.
- Logs function name, error type, and inputs on failure.
- Optional `filename` argument to log to a file instead of the console.

## Testing
Run tests with coverage:
```bash
pytest --cov=src --cov-report=term-missing
```
HTML coverage reports are saved in the `htmlcov/` directory.

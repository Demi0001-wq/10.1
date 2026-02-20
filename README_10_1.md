# Bank Operations Widget

## Description
This project implements a widget for processing banking operations. It provides utility functions for filtering transactions by state and sorting them by date.

## Features
- **Filter by State**: Extract transactions based on their status (e.g., 'EXECUTED', 'CANCELED').
- **Sort by Date**: Order transactions chronologically or reverse-chronologically.
- **Search Logic**: Search through transaction descriptions using regular expressions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Demi0001-wq/10.1.git
   ```
2. Setup virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

### Filtering by state
```python
from src.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]

executed_only = filter_by_state(data, 'EXECUTED')
```

### Sorting by date
```python
from src.processing import sort_by_date

sorted_data = sort_by_date(data, reverse=True)
```

## Testing
Run tests using pytest:
```bash
pytest tests/test_processing.py
```

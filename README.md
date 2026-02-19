Banking Operations Widget

Banking utility for masking data, processing transactions, and logging.

Features
Masking card and account numbers
Filtering and sorting transactions
Efficient iterative processing
Automated function logging

How to Run

1 Install Dependencies
pip install requests python-dotenv

2 Set Up API Key
Create .env file and add API_KEY=your_key

3 Example Usage
from src.utils import get_transactions
from src.external_api import convert_to_rub

transactions = get_transactions("data/operations.json")
if transactions:
    print(convert_to_rub(transactions[0]))

Testing
pytest --cov=src --cov-report=term-missing

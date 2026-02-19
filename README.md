Banking Operations Widget

Banking utility for masking data, processing transactions, and logging.

Features
Masking card and account numbers
Filtering and sorting transactions
Iterative processing with generators
Automated function logging
CSV and Excel file reading support
Regular expression search

How to Run

1 Install Dependencies
pip install pandas openpyxl requests python-dotenv

2 Set Up API Key
Create .env file and add API_KEY=your_key

3 Example Usage
python main.py

Testing
pytest --cov=src --cov-report=term-missing

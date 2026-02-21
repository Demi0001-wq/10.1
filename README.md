# E-commerce Django Project

This project is a web application for an e-commerce platform built using the Django framework. It includes a `catalog` application to manage products and categories.

## Features

- **Store Catalog**: View products and categories through a web interface.
- **Home Page**: Welcome screen for the e-commerce store.
- **Contacts Page**: Contact information for the store.
- **Admin Interface**: Manage data via the Django admin panel.

## Installation

### Prerequisites
- Python 3.11+
- Poetry (optional, for dependency management)

### Setup with requirements.txt
1. Clone the repository and navigate to the project root.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/macOS: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Access the application at `http://127.0.0.1:8000/`.

## Testing

Run tests using `pytest`:
```bash
pytest
```

# Catalog Store - Django Project

This is a professional Django-based web application for an online product catalog.

## Project Structure
- `catalog/` - The web application for products and categories.
- `config/` - The core project settings and URL configuration.
- `manage.py` - Django's command-line utility for administrative tasks.
- `requirements.txt` - Project dependencies.

## Installation and Setup
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file for database configuration (refer to `.env.sample`).
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Populate the database with initial data:
   ```bash
   python manage.py fill
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

Visit the application at `http://127.0.0.1:8000/`

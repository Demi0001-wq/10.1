# Demi Catalog - Django E-commerce Project

This is a Django-based web application designed for managing a product catalog. The project allows users to browse products, view categories, and submit contact information.

## Project Structure

- **catalog/**: The main application containing product and category management.
  - **models.py**: Definitions for `Product`, `Category`, and `Contact`.
  - **views.py**: Controllers for Home Page and Contacts Page.
  - **apps.py**: Django application configuration.
  - **management/commands/**: Custom management commands (e.g., `fill` to populate the database).
- **config/**: Project settings and root URL configuration.
- **templates/**: HTML templates using Bootstrap styles.

## Prerequisites

- Python 3.11+
- PostgreSQL (for Database)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd demi
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on Unix/macOS:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory based on `.env.sample`.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **(Optional) Load Test Data**:
   ```bash
   python manage.py fill
   ```

7. **Start Server**:
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`.

## Author
Developed as part of the Django web development course.

# Online Catalog Project

Hi! This is my project for the Django course. It is a simple catalog store where I use PostgreSQL and Django ORM to manage products and categories.

## What is in the project
- catalog: The main folder with my models and views.
- config: The folder with Django settings.
- manage.py: Used to run the site.

## How to set it up
1. Create a virtual environment and activate it.
2. Install the requirements:
   pip install -r requirements.txt
3. Set up your .env file with your database password (you can use .env.sample as a guide).
4. Run migrations:
   python manage.py migrate
5. (Optional) You can fill the database with my test data:
   python manage.py fill
6. Start the site:
   python manage.py runserver

You can then see the site at http://127.0.0.1:8000/

By Student

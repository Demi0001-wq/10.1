# My Django Catalog Project

Hello! This is my homework project. I used Django and PostgreSQL to make a product catalog.

In this project you can find:
- catalog: The main folder with my models and views.
- config: The folder with Django settings.
- src and tests: My previous homework code.

How to start the project:
1. Install everything with: pip install -r requirements.txt
2. Create a .env file. I added .env.sample so you know what to put there. Remember to add your database password.
3. Run migrations: python manage.py migrate
4. (Optional) You can fill the database with test data: python manage.py fill
5. Start the site: python manage.py runserver

You can then see the site at http://127.0.0.1:8000/

The admin login I created is:
User: admin
Pass: admin

Thank you!

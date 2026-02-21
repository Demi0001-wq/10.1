# My Django Catalog Project

Hello! This is my homework project. I used Django and PostgreSQL to make a product catalog.

Folders in this project:
- catalog: This is my main app where I have models and views.
- config: This has the Django settings.
- src and tests: This is my old code from the first assignments.

How to start the project:
1. Install everything with: pip install -r requirements.txt
2. Create a .env file. You can look at .env.sample to see what to put there (don't forget your database password).
3. Run migrations: python manage.py migrate
4. (Optional) Load my test stickers and gadgets: python manage.py fill
5. Start the server: python manage.py runserver

Then you can go to http://127.0.0.1:8000/ to see the site.

The admin login is:
User: admin
Pass: admin

Thank you!

import json
import os
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Fill database with test data'

    def handle(self, *args, **options):
        # 1. Pre-deleting data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Sample data if fixtures are not found
        # In a real scenario, we would load from a JSON file
        categories_data = [
            {"name": "Смартфоны", "description": "Современные гаджеты"},
            {"name": "Одежда", "description": "Стильная одежда для всех"},
        ]

        products_data = [
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "200MP камера, стилус",
                "price": 180000.0,
                "category": "Смартфоны"
            },
            {
                "name": "Iphone 15",
                "description": "A16 Bionic, USB-C",
                "price": 210000.0,
                "category": "Смартфоны"
            },
            {
                "name": "Футболка",
                "description": "100% хлопок",
                "price": 1500.0,
                "category": "Одежда"
            }
        ]

        # 3. Create Categories
        category_objects = []
        for cat in categories_data:
            category_objects.append(Category.objects.create(**cat))

        # 4. Create Products
        for prod_data in products_data:
            category_name = prod_data.pop('category')
            category = Category.objects.get(name=category_name)
            Product.objects.create(category=category, **prod_data)

        self.stdout.write(self.style.SUCCESS('Successfully filled database'))

from src.product import Product
from src.category import Category
from src.exceptions import QuantityError

if __name__ == '__main__':
    print("--- 1. ZERO QUANTITY VALIDATION (INIT) ---")
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except (ValueError, QuantityError) as e:
        print(f"Перехвачена ожидаемая ошибка при создании: {e}")

    print("\n--- 2. CATEGORY ADDITION WITH NOTIFICATIONS ---")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category = Category("Смартфоны", "Категория смартфонов")
    
    # This should trigger "Товар успешно добавлен" and "Обработка добавления товара завершена"
    category.add_product(product1)

    print("\n--- 3. METRICS AND EMPTY CATEGORIES ---")
    print(f"Средняя цена в категорий '{category.name}': {category.middle_price()}")

    category_empty = Category("Пустая категория", "Без товаров", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()}")

    print("\n--- 4. FAILED ADDITION NOTIFICATION ---")
    try:
        # We manually bypass the init check for demo (if it was possible)
        # but add_product also checks.
        category.add_product("Not a Product") # type: ignore
    except (TypeError, QuantityError):
        pass # Logging handled inside add_product

from src.product import Product
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Demonstration of JSON loading
    from src.utils import load_data
    import os
    
    json_path = os.path.join("..", "..", "..", "..", "..", "Downloads", "products.json")
    # Actually, the user provided the absolute path: C:\Users\DELL\Downloads\products.json
    # But since I'm in ecommerce/ subfolder, I can use the absolute path or relative.
    # User said: "C:\Users\DELL\Downloads\products.json"
    abs_json_path = r"C:\Users\DELL\Downloads\products.json"
    
    if os.path.exists(abs_json_path):
        print("\n--- Loading data from JSON ---")
        # Reset counters for demonstration if needed, but the original script doesn't
        # Actually, the task says "Class attributes should be filled automatically when a new object is initialized."
        # So we expect counts to increase.
        
        loaded_categories = load_data(abs_json_path)
        for cat in loaded_categories:
            print(f"Категория: {cat.name}, Продуктов: {len(cat.products)}")
        
        print(f"Общее количество категорий: {Category.category_count}")
        print(f"Общее количество продуктов: {Category.product_count}")

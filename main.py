from src.product import Product
from src.category import Category
from src.product_iterator import ProductIterator

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("--- Проверка строкового представления ---")
    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("\n--- Проверка категории ---")
    print(str(category1))
    print(category1.products)

    print("--- Проверка сложения товаров ---")
    print(f"Суммарная стоимость: {product1 + product3}")

    print("\n--- Проверка итератора ---")
    it = ProductIterator(category1)
    for prod in it:
        print(prod)

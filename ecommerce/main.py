from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.order import Order

if __name__ == '__main__':
    print("--- 1. MIXIN LOGGING DEMONSTRATION ---")
    # Initializing products will trigger the PrintMixin console log via super()
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Smartphone("Iphone 15", "512GB, Gray space", 120000.0, 10, 95.5, "15 Pro", 512, "Titanium Blue")
    p3 = LawnGrass("Газон", "Зеленый газон", 500.0, 50, "NL", "14d", "Green")

    print("\n--- 2. CATEGORY & ABSTRACTION ---")
    category = Category("Electronics", "High-tech gadgets", [p1, p2])
    print(str(category))
    print(category.products)

    print("\n--- 3. ORDER CLASS ADAPTATION ---")
    order = Order(p3, 2)
    print(str(order))
    print(f"Products in order: {order.products}")

    print("\n--- 4. TYPE SAFETY VERIFICATION ---")
    try:
        Order("Not a Product instance", 1)  # type: ignore
    except TypeError as e:
        print(f"Confirmed safety catch for Order: {e}")

    try:
        category.add_product("Not a Product instance") # type: ignore
    except TypeError as e:
        print(f"Confirmed safety catch for Category: {e}")

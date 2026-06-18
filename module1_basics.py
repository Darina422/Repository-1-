# module1_basics.py - Базовые типы данных, переменные и ввод/вывод

# Задача 1. Работа с переменными разных типов
user_name = "Анна"              # строковый тип
user_age = 22                   # целочисленный тип
user_height = 1.68              # вещественный тип
is_active_user = True           # булевый тип

# Вывод информации о пользователе
print("=== Информация о пользователе ===")
print(f"Имя: {user_name} (тип: {type(user_name).__name__})")
print(f"Возраст: {user_age} (тип: {type(user_age).__name__})")
print(f"Рост: {user_height} (тип: {type(user_height).__name__})")
print(f"Активен: {is_active_user} (тип: {type(is_active_user).__name__})")

# Задача 2. Ввод данных с клавиатуры и преобразование типов
favorite_number_input = input("\nВведите ваше любимое число: ")
favorite_number = int(favorite_number_input)  # преобразуем строку в число

# Вычисляем квадрат, куб и корень числа
number_square = favorite_number ** 2
number_cube = favorite_number ** 3
number_sqrt = favorite_number ** 0.5

print(f"Квадрат числа {favorite_number}: {number_square}")
print(f"Куб числа {favorite_number}: {number_cube}")
print(f"Квадратный корень из {favorite_number}: {number_sqrt:.2f}")

# Задача 3. Работа со списками и словарями
product_categories = ["Электроника", "Одежда", "Продукты", "Книги"]  # список
product_prices = {"Телефон": 50000, "Наушники": 3000, "Книга": 500}  # словарь

print("\n=== Категории товаров ===")
for category in product_categories:
    print(f"- {category}")

print("\n=== Цены на товары ===")
for product, price in product_prices.items():
    print(f"{product}: {price} руб.")

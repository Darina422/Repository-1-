# module2_conditions.py - Условные операторы и циклы

# Задача 1. Проверка возраста для доступа к контенту
user_age_input = input("Введите ваш возраст: ")
user_age = int(user_age_input)

if user_age < 18:
    access_status = "Доступ к контенту запрещён (возрастное ограничение 18+)"
elif 18 <= user_age <= 65:
    access_status = "Доступ к контенту разрешён"
else:
    access_status = "Доступ разрешён, но рекомендуется подтверждение личности"

print(f"Статус: {access_status}")

# Задача 2. Цикл for - таблица умножения для выбранного числа
multiplier_input = input("\nВведите число для таблицы умножения: ")
multiplier = int(multiplier_input)

print(f"\n=== Таблица умножения на {multiplier} ===")
for i in range(1, 11):
    result = multiplier * i
    print(f"{multiplier} × {i} = {result}")

# Задача 3. Цикл while - игра "Угадай число"
import random

secret_number = random.randint(1, 10)
attempts_count = 0
max_attempts = 5

print("\n=== Игра 'Угадай число' (от 1 до 10) ===")
print(f"У вас {max_attempts} попыток!")

while attempts_count < max_attempts:
    guess_input = input("Ваше предположение: ")
    guess = int(guess_input)
    attempts_count += 1
    
    if guess == secret_number:
        print(f"Поздравляю! Вы угадали число {secret_number} с {attempts_count} попытки!")
        break
    elif guess < secret_number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    
    remaining_attempts = max_attempts - attempts_count
    if remaining_attempts > 0:
        print(f"Осталось попыток: {remaining_attempts}")

if attempts_count == max_attempts and guess != secret_number:
    print(f"Игра окончена! Было загадано число {secret_number}")

# Задача 4. Поиск элемента в списке
available_colors = ["красный", "синий", "зеленый", "желтый", "белый", "черный"]
search_color = input("\nВведите цвет для поиска: ").lower().strip()

if search_color in available_colors:
    color_index = available_colors.index(search_color)
    print(f"Цвет '{search_color}' найден на позиции {color_index + 1}")
else:
    print(f"Цвета '{search_color}' нет в списке доступных цветов")

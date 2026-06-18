# module3_functions.py - Определение и вызов функций

def format_user_greeting(user_name, greeting_text="Здравствуйте"):
    """
    Формирует приветственное сообщение для пользователя
    Параметры:
        user_name (str): имя пользователя
        greeting_text (str): текст приветствия (по умолчанию "Здравствуйте")
    Возвращает:
        str: отформатированное приветствие
    """
    return f"{greeting_text}, {user_name}!"

def calculate_list_average(numbers_list):
    """
    Вычисляет среднее арифметическое списка чисел
    Параметры:
        numbers_list (list): список чисел
    Возвращает:
        float: среднее значение (0 если список пуст)
    """
    if not numbers_list:
        return 0.0
    total_sum = sum(numbers_list)
    count_elements = len(numbers_list)
    return total_sum / count_elements

def reverse_string(text_string):
    """
    Переворачивает строку (реверсирует символы)
    Параметры:
        text_string (str): исходная строка
    Возвращает:
        str: перевёрнутая строка
    """
    return text_string[::-1]

def is_word_palindrome(word_string):
    """
    Проверяет, является ли слово палиндромом (читается одинаково слева направо и справа налево)
    Параметры:
        word_string (str): слово для проверки
    Возвращает:
        bool: True если палиндром, иначе False
    """
    word_cleaned = word_string.lower().replace(" ", "")
    return word_cleaned == word_cleaned[::-1]

def main():
    # Демонстрация работы функций
    print("=== Работа с функциями ===")
    
    # Функция приветствия
    print(format_user_greeting("Алексей"))
    print(format_user_greeting("Мария", "Приветствую"))
    
    # Функция вычисления среднего
    test_numbers = [15, 25, 35, 45, 55]
    average_value = calculate_list_average(test_numbers)
    print(f"\nСреднее значение чисел {test_numbers}: {average_value:.2f}")
    
    # Функция реверсирования строки
    original_text = "Python"
    reversed_text = reverse_string(original_text)
    print(f"Исходная строка: {original_text}")
    print(f"Перевёрнутая строка: {reversed_text}")
    
    # Функция проверки палиндрома
    test_word = input("\nВведите слово для проверки на палиндром: ")
    if is_word_palindrome(test_word):
        print(f"Слово '{test_word}' является палиндромом!")
    else:
        print(f"Слово '{test_word}' не является палиндромом.")

if __name__ == "__main__":
    main()

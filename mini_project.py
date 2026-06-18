# mini_project.py - Итоговый проект: Система управления библиотекой книг

# Глобальные переменные
book_collection = []  # список книг в библиотеке

def display_menu():
    """Отображает главное меню программы"""
    print("\n" + "="*40)
    print("      СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
    print("="*40)
    print("1. Показать все книги")
    print("2. Добавить новую книгу")
    print("3. Удалить книгу по названию")
    print("4. Отметить книгу как прочитанную")
    print("5. Поиск книги по автору")
    print("6. Статистика библиотеки")
    print("7. Выйти из программы")
    print("="*40)

def display_all_books():
    """Выводит список всех книг в библиотеке"""
    if not book_collection:
        print("\n📚 Библиотека пуста. Добавьте книги!")
        return
    
    print("\n=== СПИСОК КНИГ ===")
    print(f"Всего книг: {len(book_collection)}")
    print("-" * 50)
    
    for index, book in enumerate(book_collection, start=1):
        read_status = "✓ Прочитана" if book["is_read"] else "○ Не прочитана"
        print(f"{index}. {book['title']}")
        print(f"   Автор: {book['author']}")
        print(f"   Год: {book['year']}")
        print(f"   Статус: {read_status}")
        print("-" * 50)

def add_new_book():
    """Добавляет новую книгу в библиотеку"""
    print("\n=== ДОБАВЛЕНИЕ НОВОЙ КНИГИ ===")
    
    book_title = input("Введите название книги: ").strip()
    if not book_title:
        print("❌ Название не может быть пустым!")
        return
    
    book_author = input("Введите автора книги: ").strip()
    if not book_author:
        print("❌ Автор не может быть пустым!")
        return
    
    # Проверка ввода года
    try:
        year_input = input("Введите год издания: ")
        book_year = int(year_input)
        if book_year < 0 or book_year > 2026:
            print("❌ Некорректный год! Должен быть от 0 до 2026")
            return
    except ValueError:
        print("❌ Введите число!")
        return
    
    # Добавляем книгу в коллекцию
    new_book = {
        "title": book_title,
        "author": book_author,
        "year": book_year,
        "is_read": False
    }
    book_collection.append(new_book)
    print(f"✅ Книга '{book_title}' успешно добавлена!")

def delete_book_by_title():
    """Удаляет книгу по названию"""
    if not book_collection:
        print("\n❌ Библиотека пуста, нечего удалять!")
        return
    
    book_title = input("\nВведите название книги для удаления: ").strip().lower()
    
    for index, book in enumerate(book_collection):
        if book["title"].lower() == book_title:
            removed_book = book_collection.pop(index)
            print(f"✅ Книга '{removed_book['title']}' удалена!")
            return
    
    print(f"❌ Книга с названием '{book_title}' не найдена!")

def mark_book_as_read():
    """Отмечает книгу как прочитанную по названию"""
    if not book_collection:
        print("\n❌ Библиотека пуста!")
        return
    
    book_title = input("\nВведите название книги, которую прочитали: ").strip().lower()
    
    for book in book_collection:
        if book["title"].lower() == book_title:
            if book["is_read"]:
                print(f"📖 Книга '{book['title']}' уже отмечена как прочитанная")
            else:
                book["is_read"] = True
                print(f"✅ Книга '{book['title']}' отмечена как прочитанная!")
            return
    
    print(f"❌ Книга с названием '{book_title}' не найдена!")

def search_books_by_author():
    """Поиск книг по автору"""
    if not book_collection:
        print("\n❌ Библиотека пуста!")
        return
    
    author_name = input("\nВведите имя автора для поиска: ").strip().lower()
    found_books = []
    
    for book in book_collection:
        if author_name in book["author"].lower():
            found_books.append(book)
    
    if found_books:
        print(f"\n=== КНИГИ АВТОРА {author_name.title()} ===")
        for book in found_books:
            status = "✓ Прочитана" if book["is_read"] else "○ Не прочитана"
            print(f"- {book['title']} ({book['year']}) - {status}")
    else:
        print(f"❌ Книг автора '{author_name}' не найдено!")

def show_library_statistics():
    """Показывает статистику библиотеки"""
    if not book_collection:
        print("\n📊 Библиотека пуста. Статистика недоступна.")
        return
    
    total_books = len(book_collection)
    read_books = sum(1 for book in book_collection if book["is_read"])
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    
    # Поиск самого старого и нового года
    years = [book["year"] for book in book_collection]
    oldest_year = min(years)
    newest_year = max(years)
    
    # Сбор авторов
    authors = {}
    for book in book_collection:
        authors[book["author"]] = authors.get(book["author"], 0) + 1
    most_popular_author = max(authors, key=authors.get) if authors else "Нет данных"
    
    print("\n=== СТАТИСТИКА БИБЛИОТЕКИ ===")
    print(f"📚 Всего книг: {total_books}")
    print(f"✅ Прочитано книг: {read_books} ({read_percentage:.1f}%)")
    print(f"📖 Не прочитано: {unread_books}")
    print(f"📅 Самая старая книга: {oldest_year} год")
    print(f"📅 Самая новая книга: {newest_year} год")
    print(f"👤 Самый популярный автор: {most_popular_author} ({authors[most_popular_author]} книг)")

def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему управления библиотекой!")
    
    while True:
        display_menu()
        user_choice = input("\nВыберите действие (1-7): ").strip()
        
        if user_choice == "1":
            display_all_books()
        elif user_choice == "2":
            add_new_book()
        elif user_choice == "3":
            delete_book_by_title()
        elif user_choice == "4":
            mark_book_as_read()
        elif user_choice == "5":
            search_books_by_author()
        elif user_choice == "6":
            show_library_statistics()
        elif user_choice == "7":
            print("\n👋 До свидания! Спасибо за использование программы!")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, выберите номер от 1 до 7.")

if __name__ == "__main__":
    main()

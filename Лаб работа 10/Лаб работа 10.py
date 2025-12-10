import json
import csv

# --- Функции ---
def add_books():
    books = []
    try:
        n = int(input("Введите количество книг: "))
        for i in range(n):
            title = input(f"\nНазвание книги {i+1}: ")
            author = input("Автор: ")
            price = float(input("Цена (в тенге): "))
            books.append({"title": title, "author": author, "price": price})
        return books
    except ValueError:
        print("Ошибка: введите корректное число!")
        return []

def save_to_txt(books):
    try:
        with open("books.txt", "w", encoding="utf-8") as f:
            for b in books:
                f.write(f"{b['title']} | {b['author']} | {b['price']}\n")
        print("✅ Данные сохранены в books.txt")
    except Exception as e:
        print("Ошибка при сохранении:", e)

def save_to_json(books):
    try:
        with open("books.json", "w", encoding="utf-8") as jf:
            json.dump(books, jf, ensure_ascii=False, indent=4)
        print("✅ Данные сериализованы в books.json")
    except Exception as e:
        print("Ошибка при сериализации:", e)

def save_to_csv(books):
    try:
        with open("books.csv", "w", newline="", encoding="utf-8") as cf:
            writer = csv.DictWriter(cf, fieldnames=["title", "author", "price"])
            writer.writeheader()
            writer.writerows(books)
        print("✅ Данные сохранены в books.csv")
    except Exception as e:
        print("Ошибка при сохранении CSV:", e)

def load_from_txt():
    try:
        with open("books.txt", "r", encoding="utf-8") as f:
            print("\n📚 Содержимое books.txt:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Файл books.txt не найден.")

def filter_books(books):
    try:
        min_price = float(input("Введите минимальную цену: "))
        filtered = [b for b in books if b["price"] >= min_price]
        print("\nКниги дороже порога:")
        for b in filtered:
            print(f"{b['title']} ({b['author']}) — {b['price']} тг")
    except ValueError:
        print("Ошибка: цена должна быть числом.")

def sort_books(books):
    return sorted(books, key=lambda x: x["price"], reverse=True)

# --- Главное меню ---
def main():
    books = []
    while True:
        print("\nМеню:")
        print("1. Добавить книги")
        print("2. Показать книги (из памяти)")
        print("3. Сохранить в файлы (txt, json, csv)")
        print("4. Прочитать из txt")
        print("5. Отфильтровать по цене")
        print("6. Сортировать по цене (по убыванию)")
        print("7. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            books = add_books()
        elif choice == "2":
            if books:
                for b in books:
                    print(f"{b['title']} — {b['author']} — {b['price']} тг")
            else:
                print("Список пуст.")
        elif choice == "3":
            save_to_txt(books)
            save_to_json(books)
            save_to_csv(books)
        elif choice == "4":
            load_from_txt()
        elif choice == "5":
            filter_books(books)
        elif choice == "6":
            books = sort_books(books)
            print("✅ Книги отсортированы.")
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
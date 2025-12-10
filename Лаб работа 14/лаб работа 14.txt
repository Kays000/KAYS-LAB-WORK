import logging
from typing import List, Union

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.WARNING)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def calculate_average(grades: List[Union[int, float]]) -> float:
    """Вычисляет средний балл (0–100)."""

    if not grades:
        logger.error("Список оценок пуст")
        raise ValueError("Список оценок не может быть пустым")

    if not all(isinstance(x, (int, float)) for x in grades):
        logger.error("В списке есть нечисловые значения: %s", grades)
        raise TypeError("Все значения должны быть числами")

    if any(x < 0 or x > 100 for x in grades):
        logger.error("Оценки вне диапазона 0–100: %s", grades)
        raise ValueError("Оценки должны быть в диапазоне 0–100")

    avg = round(sum(grades) / len(grades), 2)
    logger.info(f"Средний балл вычислен: {avg}")
    return avg


def determine_grade_letter(avg: float) -> str:
    """Определяет буквенную оценку."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


def student_report(name: str, grades: List[Union[int, float]]) -> str:
    """Формирует отчёт о студенте."""
    avg = calculate_average(grades)
    letter = determine_grade_letter(avg)

    logger.info(f"Создан отчёт для студента {name}")
    return f"Студент: {name}\nСредний балл: {avg}\nОценка: {letter}"

def print_table(students: List[dict]):
    """Выводит таблицу всех студентов."""

    if not students:
        print("\nТаблица пуста.\n")
        return

    print("\n===================== ТАБЛИЦА СТУДЕНТОВ =====================")
    print(f"{'Имя':<20} {'Средний балл':<15} {'Оценка':<10}")
    print("-" * 55)

    for student in students:
        print(f"{student['name']:<20} {student['avg']:<15} {student['letter']:<10}")

    print("=" * 55 + "\n")


def save_table(students: List[dict], filename="students.txt"):
    """Сохраняет таблицу в текстовый файл."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{'Имя':<20} {'Средний балл':<15} {'Оценка':<10}\n")
            f.write("-" * 55 + "\n")
            for s in students:
                f.write(f"{s['name']:<20} {s['avg']:<15} {s['letter']:<10}\n")

        print(f"\nТаблица успешно сохранена в файл: {filename}\n")
    except Exception as e:
        print("Ошибка при сохранении файла:", e)
        logger.exception("Ошибка при сохранении таблицы")

def main_menu():
    students = []  # список всех студентов

    while True:
        print("========== М Е Н Ю ==========")
        print("1 — Добавить студента")
        print("2 — Показать таблицу студентов")
        print("3 — Сохранить таблицу в файл")
        print("4 — Выход")
        print("==============================")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            try:
                name = input("Введите имя студента: ").strip()
                grades_input = input("Введите оценки через пробел (0–100): ").split()
                grades = [float(x) for x in grades_input]

                avg = calculate_average(grades)
                letter = determine_grade_letter(avg)

                students.append({
                    "name": name,
                    "avg": avg,
                    "letter": letter
                })

                print("\nСтудент успешно добавлен!")
                print(student_report(name, grades))
                print()

            except Exception as e:
                print("Ошибка:", e)
                logger.exception("Ошибка при добавлении студента")

        elif choice == "2":
            print_table(students)

        elif choice == "3":
            save_table(students)

        elif choice == "4":
            print("Выход из программы...")
            break

        else:
            print("Неверный пункт меню. Повторите.")

if __name__ == "__main__":
    main_menu()
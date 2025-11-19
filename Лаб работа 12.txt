import json

class Student:
    def __init__(self, name, group, gpa):
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть от 0 до 4.")

    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}")


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Студент добавлен!")

    def remove_student(self, name):
        for s in self.students:
            if s.get_name() == name:
                self.students.remove(s)
                print("Студент удалён!")
                return
        print("Студент не найден.")

    def show_all(self):
        if not self.students:
            print("Список студентов пуст.")
            return
        print("\n--- СПИСОК СТУДЕНТОВ ---")
        for s in self.students:
            s.display_info()

    def get_top_students(self, threshold):
        print(f"\nСтуденты с GPA выше {threshold}:")
        found = False
        for s in self.students:
            if s.get_gpa() > threshold:
                s.display_info()
                found = True
        if not found:
            print("Нет таких студентов.")

    def save_to_json(self, filename="students.json"):
        data = [
            {
                "name": s.get_name(),
                "group": s.get_group(),
                "gpa": s.get_gpa()
            }
            for s in self.students
        ]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Данные сохранены в students.json")


def menu():
    print("\n=== СИСТЕМА УЧЁТА СТУДЕНТОВ ===")
    print("1. Добавить студента")
    print("2. Удалить студента")
    print("3. Показать всех студентов")
    print("4. Показать студентов с высоким GPA")
    print("5. Сохранить в JSON")
    print("0. Выход")

group = Group()

while True:
    menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        group_name = input("Группа: ")
        gpa = float(input("GPA (0–4): "))
        student = Student(name, group_name, gpa)
        group.add_student(student)

    elif choice == "2":
        name = input("Введите имя студента: ")
        group.remove_student(name)

    elif choice == "3":
        group.show_all()

    elif choice == "4":
        threshold = float(input("Порог GPA: "))
        group.get_top_students(threshold)

    elif choice == "5":
        group.save_to_json()

    elif choice == "0":
        print("Выход из программы...")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
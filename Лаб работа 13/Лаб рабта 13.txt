class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


class Student(Person):
    def __init__(self, name, age, group, gpa):
        super().__init__(name, age)
        self.group = group
        self.gpa = gpa

    def display_info(self):
        print(f"Студент: {self.name}, Возраст: {self.age}, Группа: {self.group}, GPA: {self.gpa}")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        print(f"Преподаватель: {self.name}, Возраст: {self.age}, "
              f"Предмет: {self.subject}, Стаж: {self.experience} лет")


class AdminStaff(Person):
    def __init__(self, name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def display_info(self):
        print(f"Админ. сотрудник: {self.name}, Возраст: {self.age}, "
              f"Должность: {self.position}, Отдел: {self.department}")


# ==================== МЕНЮ ====================

def main():
    people = []

    while True:
        print("\n=== Учебное заведение ===")
        print("1. Добавить студента")
        print("2. Добавить преподавателя")
        print("3. Добавить административного сотрудника")
        print("4. Показать всех")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Имя: ")
            age = int(input("Возраст: "))
            group = input("Группа: ")
            gpa = float(input("GPA: "))
            people.append(Student(name, age, group, gpa))

        elif choice == "2":
            name = input("Имя: ")
            age = int(input("Возраст: "))
            subject = input("Предмет: ")
            experience = int(input("Стаж (лет): "))
            people.append(Teacher(name, age, subject, experience))

        elif choice == "3":
            name = input("Имя: ")
            age = int(input("Возраст: "))
            position = input("Должность: ")
            department = input("Отдел: ")
            people.append(AdminStaff(name, age, position, department))

        elif choice == "4":
            if not people:
                print("Список пуст.")
            else:
                print("\n--- Список персонала ---")
                for p in people:
                    p.display_info()

        elif choice == "0":
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()
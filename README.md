a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /, //, %, **): ")
if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка: деление на ноль!")
elif op == "//":
    if b != 0:
        print("Результат:", a // b)
    else:
        print("Ошибка: деление на ноль!")
elif op == "%":
    if b != 0:
        print("Результат:", a % b)
    else:
        print("Ошибка: деление на ноль!")
elif op == "**":
    print("Результат:", a ** b)
else:
    print("Неизвестная операция")
<img width="1691" height="704" alt="Снимок экрана 2025-09-03 145628" src="https://github.com/user-attachments/assets/9deed7fc-6fb4-46cb-ad43-f1f4668bb610" />

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
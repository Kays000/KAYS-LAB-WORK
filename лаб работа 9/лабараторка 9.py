# задание 1

def print_numbers(n):
    # Базовое условие — когда дошли до 1
    if n == 1:
        print(1)
    else:
        print_numbers(n - 1)  # уменьшаем n
        print(n)  # выводим текущее число
print_numbers(5)

# задание 2

def count_chars(s):
    # Базовое условие — если строка пустая
    if s == "":
        return 0
    # Рекурсивное уменьшение: убираем первый символ и считаем оставшиеся
    return 1 + count_chars(s[1:])
text = "лабараторка"
print("Количество символов:", count_chars(text))

# задание 3

a = int(input())
b = int(input())
def power(a, b):
    # Базовое условие — степень 0
    if b == 0:
        return 1
    # Рекурсивное уменьшение показателя
    return a * power(a, b - 1)
print(a," в степени ",b, "=", power(a, b))

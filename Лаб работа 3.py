print("числа от 1 до 10 (for)")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

print("сумма чисел от 1 до 100 (while)")
i = 1
s = 0
while i <= 100:
    s += i
    i += 1
print("Сумма =", s)
print()

print("таблица умножения (вложенные циклы)")
for i in range(1, 6):      
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ") 
    print()
print()

print("обработка массива")
A = [3, -5, 7, 10, -2, 4]
print("Исходный массив:", A)

for i in range(len(A)):
    if A[i] > 0:
        A[i] = 0   

print("Измененный массив:", A)

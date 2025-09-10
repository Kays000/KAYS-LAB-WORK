import random
A = [random.randint(-20, 20) for _ in range(50)]
print("Исходный массив A:")
print(A)
for i in range(len(A)):
    if A[i] > 0:           
        A[i] = i          
    if A[i] > 10:         
        A[i] -= 2         
print("\nПреобразованный массив A:")
print(A)


B = [[random.randint(-20, 20) for _ in range(4)] for _ in range(4)]
print("\nДвумерный массив B:")
for row in B:
    print(row)

diagonal = [B[i][i] for i in range(4)]
min_elem = min(diagonal)

print("\nЭлементы главной диагонали:", diagonal)
print("Наименьший элемент диагонали:", min_elem)

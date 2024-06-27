import random

# Указанные размеры и диапазон значений
n, m = 5, 5
r1, r2 = -100, 100

# Создание и заполнение массива случайными числами
A = [[random.randint(r1, r2) for _ in range(m)] for _ in range(n)]

# Вывод исходного массива
print("Исходный массив:")
for row in A:
    print(row)

# Проверка на наличие строки с ровно двумя отрицательными элементами
found = False
for i, row in enumerate(A):
    negative_count = sum(1 for x in row if x < 0)
    if negative_count == 2:
        found = True
        print(f"Строка {i} содержит ровно два отрицательных элемента.")

if not found:
    print("Строк с двумя отрицательными элементами в массиве нет.")

print('\n\nЗадание выполнил студент 1-го курса\n2023-ФГиИБ-ПИ-1б\nКорязов Дмитрий')

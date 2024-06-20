import random

def create_array(n, m, r1, r2):
    """Создает и заполняет двумерный массив случайными числами из диапазона (r1, r2)"""
    return [[random.randint(r1, r2) for _ in range(m)] for _ in range(n)]

def count_negatives(row):
    """Считает количество отрицательных элементов в строке"""
    count = 0
    for x in row:
        if x < 0:
            count += 1
    return count

def print_array(A):
    """Выводит двумерный массив"""
    for row in A:
        print(row)

def find_row_with_two_negatives(A):
    """Находит и выводит номера строк с ровно двумя отрицательными элементами"""
    found = False
    for i, row in enumerate(A):
        if count_negatives(row) == 2:
            found = True
            print(f"Строка {i} содержит ровно два отрицательных элемента.")
    if not found:
        print("Строк с двумя отрицательными элементами в массиве нет.")

# Указанные размеры и диапазон значений
n, m = 5, 5
r1, r2 = -100, 100

# Создание массива
A = create_array(n, m, r1, r2)

# Вывод исходного массива
print("Исходный массив:")
print_array(A)

# Поиск строки с ровно двумя отрицательными элементами
find_row_with_two_negatives(A)

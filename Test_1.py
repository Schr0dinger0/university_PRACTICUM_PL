import math

# Определение функции f(x)
def f(x):
    return 5 * math.sin(x)**2 + math.cos(3 * x)

# Табулирование функции
x0 = 2
xn = 8
hx = 0.20

x_values = []
f_values = []

x = x0
while x <= xn*1.001:
    fx = f(x)
    x_values.append(x)
    f_values.append(fx)
    x += hx

# Вывод значений с точностью 3 знака после запятой
for x, fx in zip(x_values, f_values):
    print(f"x = {x:.2f}, f(x) = {fx:.3f}")

print('\n\nЗадание выполнил студент 1-го курса\n2023-ФГиИБ-ПИ-1б\nКорязов Дмитрий')

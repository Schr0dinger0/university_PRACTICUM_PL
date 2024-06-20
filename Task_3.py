# Определение функции f(x)
def f(x):
    if x < 2*1.001:
        return 2 * abs(x) - 1
    elif 2*1.001 <= x < 4*1.001:
        return 4 * x + x**2
    else:
        return None

# Табулирование функции
x0 = -5
xn = 10
hx = 0.20

x_values = []
f_values = []

x = x0
while x <= xn:
    fx = f(x)
    if fx is not None:
        x_values.append(x)
        f_values.append(fx)
    x += hx

# Вывод значений с точностью 3 знака после запятой
for x, fx in zip(x_values, f_values):
    print(f"x = {x:.2f}, f(x) = {fx:.3f}")

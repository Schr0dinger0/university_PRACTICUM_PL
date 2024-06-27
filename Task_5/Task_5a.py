x0 = -5
xn = 10
hx = 0.2

print(f"{'x':>10} {'f(x)':>10}")
x = x0
while x <= xn:
    if x < 2*1.001:
        fx = 2 * abs(x) - 1
    elif 2*1.001 <= x <= 4*1.001:
        fx = 4 * x + x ** 2
    else:
        fx = "Функция f(x) не определена"

    if isinstance(fx, str):
        print(f"{x:>10.3f} {fx:>10}")
    else:
        print(f"{x:>10.3f} {fx:>10.3f}")

    x += hx

print('\n\nЗадание выполнил студент 1-го курса\n2023-ФГиИБ-ПИ-1б\nКорязов Дмитрий')

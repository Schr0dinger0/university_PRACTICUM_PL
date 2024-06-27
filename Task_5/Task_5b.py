def f(x):
    if x < 2*1.001:
        return 2 * abs(x) - 1
    elif 2*1.001 <= x <= 4*1.001:
        return 4 * x + x**2
    else:
        return None

def tabulate_function(x0, xn, hx):
    x = x0
    print(f"{'x':>10} {'f(x)':>10}")
    while x <= xn:
        fx = f(x)
        if fx is None:
            print(f"{x:>10.3f} {'не определена':>10}")
        else:
            print(f"{x:>10.3f} {fx:>10.3f}")
        x += hx

x0 = -5
xn = 10
hx = 0.2

tabulate_function(x0, xn, hx)

print('\n\nЗадание выполнил студент 1-го курса\n2023-ФГиИБ-ПИ-1б\nКорязов Дмитрий')

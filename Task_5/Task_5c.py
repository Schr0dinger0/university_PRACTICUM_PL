class FunctionTabulator:
    def __init__(self, x0, xn, hx):
        self.x0 = x0
        self.xn = xn
        self.hx = hx

    def f(self, x):
        if x < 2*1.001:
            return 2 * abs(x) - 1
        elif 2*1.001 <= x <= 4*1.001:
            return 4 * x + x**2
        else:
            return None

    def tabulate(self):
        x = self.x0
        print(f"{'x':>10} {'f(x)':>10}")
        while x <= self.xn:
            fx = self.f(x)
            if fx is None:
                print(f"{x:>10.3f} {'не определена':>10}")
            else:
                print(f"{x:>10.3f} {fx:>10.3f}")
            x += self.hx

x0 = -5
xn = 10
hx = 0.2

tabulator = FunctionTabulator(x0, xn, hx)
tabulator.tabulate()

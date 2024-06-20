import math

# Примеры значений x для проверки
x_values = [4, 5, 6, 7, 8, 9]

results = []
for x in x_values:
    try:
        if x ** 2 - 9 >= 0 and (x - 3) != 0:
            sqrt_part = math.sqrt(x ** 2 - 9)
            numerator_z1 = x ** 2 + 2 * x - 3 + (x + 1) * sqrt_part
            denominator_z1 = x ** 2 - 2 * x - 3 + (x - 1) * sqrt_part

            if denominator_z1 != 0:
                z1 = numerator_z1 / denominator_z1
                z2 = math.sqrt((x + 3) / (x - 3))

                results.append((x, z1, z2))
    except ValueError:
        pass

for x, z1, z2 in results:
    print(f"x = {x}: z1 = {z1:.2f}, z2 = {z2:.2f}, {'совпадают' if abs(z1 - z2) < 1e-2 else 'не совпадают'}")

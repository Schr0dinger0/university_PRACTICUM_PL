def decimal_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])


def task1():
    decimal_number = 298
    bases = [2, 16, 8]
    results = {}
    for base in bases:
        results[base] = decimal_to_base(decimal_number, base)
    return results


def task2():
    missing_digits = {}
    binary_number = "1100"

    binary_int = int(binary_number, 2)

    missing_digits['binary'] = binary_int
    return missing_digits


def task3():
    numbers = ["74_8", "84_10", "22_4", "2F_16"]
    decimal_numbers = []
    for num in numbers:
        base = int(num.split('_')[1])
        value = int(num.split('_')[0], base)
        decimal_numbers.append((value, num))
    sorted_numbers = sorted(decimal_numbers)
    return [num[1] for num in sorted_numbers]


def task4():
    numbers = {
        "A_16": int("A", 16),
        "2B_16": int("2B", 16),
        "1B_16": int("1B", 16),
        "10_16": int("10", 16),
        "15_16": int("15", 16)
    }
    even_numbers = [k for k, v in numbers.items() if v % 2 == 0]
    odd_numbers = [k for k, v in numbers.items() if v % 2 != 0]
    return even_numbers, odd_numbers


def decimal_to_ternary(n, precision=3):
    # Целая часть
    integer_part = int(n)
    # Дробная часть
    fractional_part = n - integer_part
    # Перевод целой части
    integer_part_ternary = ""
    if integer_part == 0:
        integer_part_ternary = "0"
    while integer_part > 0:
        integer_part_ternary = str(integer_part % 3) + integer_part_ternary
        integer_part //= 3
    # Перевод дробной части
    fractional_part_ternary = []
    for _ in range(precision):
        fractional_part *= 3
        fractional_part_ternary.append(str(int(fractional_part)))
        fractional_part -= int(fractional_part)
    return integer_part_ternary + '.' + ''.join(fractional_part_ternary)


def task5():
    # Десятичные дроби
    fractions = [1, 2/3, 11/27]
    # Сумма дробей
    total_sum = sum(fractions)
    # Перевод в троичную систему счисления
    ternary_sum = decimal_to_ternary(total_sum)
    return ternary_sum


def main():
    # Задание 1
    results1 = task1()
    print("\nЗадание 1:")
    print(f"298_{10} = {results1[2]}_{2}")
    print(f"298_{10} = {results1[16]}_{16}")
    print(f"298_{10} = {results1[8]}_{8}")

    # Задание 2
    results2 = task2()
    print("\nЗадание 2:")
    print(f"1100_2 = {results2['binary']}_10")

    # Задание 3
    results3 = task3()
    print("\nЗадание 3:")
    print(" ".join(results3))

    # Задание 4
    even_numbers, odd_numbers = task4()
    print("\nЗадание 4:")
    print("Четные:", " ".join(even_numbers))
    print("Нечетные:", " ".join(odd_numbers))

    # Задание 5
    result5 = task5()
    print("\nЗадание 5:")
    print(f"1 + 2/3 + 11/27 = {result5} (в троичной системе счисления)")

if __name__ == "__main__":
    main()
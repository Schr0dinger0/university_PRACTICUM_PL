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
    for x in range(2):  # Пропущенная двоичная цифра
        for y in range(10):  # Пропущенная десятичная цифра
            for z in range(8):  # Первая пропущенная восьмеричная цифра
                for w in range(8):  # Вторая пропущенная восьмеричная цифра
                    binary_str = f"1100.{x}"
                    decimal_str = f"1{y}.5"
                    octal_str = f"{z}4.{w}"

                    # Преобразование в десятичную систему
                    decimal_from_binary = int(binary_str.replace('.', ''), 2) / (2 ** len(binary_str.split('.')[1]))
                    decimal_from_decimal = float(decimal_str)
                    decimal_from_octal = int(octal_str.replace('.', ''), 8) / (8 ** len(octal_str.split('.')[1]))

                    # Проверка совпадения чисел
                    if abs(decimal_from_binary - decimal_from_decimal) < 1e-6 and abs(
                            decimal_from_decimal - decimal_from_octal) < 1e-6:
                        return f"1100.{x}(2) = 1{y}.5(10) = {z}4.{w}(8)"


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
    print("\nЗадание 2:")
    print(task2())

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

    print('\n\nЗадание выполнил студент 1-го курса\n2023-ФГиИБ-ПИ-1б\nКорязов Дмитрий')

if __name__ == "__main__":
    main()
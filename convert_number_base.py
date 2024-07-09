def conversion_decimal(number, base):
    number_decimal = 0
    intermediate_sum_parts = []
    
    print("Перевод числа в десятичную систему:")
    print(f"{number} = ", end='')

    # переводим число в десятичную систему
    for i in range(len(number)):
        digit = number[i].upper()  # Приводим к верхнему регистру
        if '0' <= digit <= '9':
            value = int(digit)
        elif 'A' <= digit <= 'F':
            value = 10 + ord(digit) - ord('A')  # Для шестнадцатеричных значений
        else:
            raise ValueError(f"Недопустимый символ '{digit}' для системы счисления с основанием {base}.")

        power = len(number) - 1 - i
        term = f"({value} × {base}^{power})"
        intermediate_sum_parts.append(term)
        number_decimal += value * (base ** power)

    # вывод результата в десятичной системе
    intermediate_sum = " + ".join(intermediate_sum_parts)
    print(f"{intermediate_sum} = {number_decimal}")
    return number_decimal

def convert_base(number_decimal, base_new):
    if base_new < 2 or base_new > 16:
        raise ValueError("Основание новой системы счисления должно быть в диапазоне от 2 до 16.")
    
    # Список для остатков
    remainder_list = []
    steps = []  # Список для сохранения шагов
    
    # Основной цикл для перевода числа
    while number_decimal > 0:
        remainder = number_decimal % base_new
        steps.append((number_decimal, base_new, number_decimal // base_new, remainder))
        remainder_list.append(remainder)
        number_decimal //= base_new
    
    # Форматированный вывод шагов
    print("\nШаги перевода:")
    for i, (current_value, base, integer_part, remainder) in enumerate(steps):
        print(f"Шаг {i + 1}: {current_value} / {base} = {integer_part}, Остаток: {remainder}")

    # Объединение остатков в строку
    if base_new == 16:
        # Для шестнадцатеричной системы преобразуем остатки в символы
        remainder_string = ''.join(['0123456789ABCDEF'[r] for r in reversed(remainder_list)])
    else:
        remainder_string = ''.join(map(str, reversed(remainder_list)))

    return remainder_string

# вводим данные
base = int(input("Выберите систему счисления (2 - двоичная, 8 - восьмеричная, 10 - десятичная, 16 - шестнадцатеричная): "))
number = input(f"Введите число в системе счисления {base}: ")

base_new = int(input("Выберите систему счисления для перевода (2 - двоичная, 8 - восьмеричная, 10 - десятичная, 16 - шестнадцатеричная): "))

# производим расчёты
print('\n')
number_decimal = conversion_decimal(number, base)
print('-' * 50)
remainder_string = convert_base(number_decimal, base_new)

# Вывод окончательного результата
print(f"\nРезультат: {remainder_string} (в системе счисления с основанием {base_new})")

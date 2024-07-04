def convert_from_decimal(number, base):

    """Преобразует десятичное число в заданную систему счисления."""

    if base == 2:
        return bin(number)[2:]  # Двоичная система
    elif base == 8:
        return oct(number)[2:]  # Восьмеричная система
    elif base == 16:
        return hex(number)[2:]  # Шестнадцатеричная система
    else:
        return str(number)  # Десятичная система

def multiplication(num1_str, num2_str, base):

    """Умножает два числа в заданной системе счисления и выводит процесс умножения в столбик."""

    # Преобразуем числа из строки в целое значение в указанной системе счисления
    num1 = int(num1_str, base)

    # Промежуточные результаты умножения
    partial_results = []

    # Выполняем умножение в столбик
    for i, digit in enumerate(reversed(num2_str)):
        digit_value = int(digit, base)
        partial_result = num1 * digit_value
        partial_result_str = convert_from_decimal(partial_result, base) + ('0' * i)
        partial_results.append(partial_result_str)

    # Определяем ширину для выравнивания
    width = max(len(pr) for pr in partial_results)

    # Вывод чисел и промежуточных результатов
    print(f"{num1_str.rjust(width)}  (number_1)")
    print(f"x {num2_str.rjust(width - 2)} (number_2)")
    print(f"{'-' * width}")  # Разделительная линия

    # Печатаем все промежуточные результаты в столбик
    for i, pr in enumerate(partial_results, start=1):
        number = pr.rjust(width)[:-i]
        if number.strip():  # Проверяем, содержит ли строка непустые символы
            print(number.upper())

    # Суммируем все промежуточные результаты
    final_result = sum(int(pr, base) for pr in partial_results)

    # Преобразуем итоговый результат обратно в заданную систему счисления
    final_result_str = convert_from_decimal(final_result, base)

    # Вывод окончательного результата
    print(f"{'-' * width}")
    print(f"{final_result_str.rjust(width).upper()}  (result)")

def addition_and_subtraction(num1_str, num2_str, base, operation):

    # Преобразование строковых чисел в целые, исходя из заданной системы счисления
    num1 = int(num1_str, base)
    num2 = int(num2_str, base)

    # Определение результата в зависимости от выбранной операции
    if operation == '+':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '-':
        result = num1 - num2
        operation_sign = '-'

    # Преобразование результата обратно в заданную систему счисления
    result_operation = convert_from_decimal(result, base)

    width = max(len(num1_str), len(num2_str), len(result_operation))

    # Вывод чисел и промежуточных результатов
    print(f"{num1_str.rjust(width).upper()}  (number_1)")
    print(f"{operation_sign} {num2_str.rjust(width - 2).upper()} (number_2)")
    print(f"{'-' * width}  (result)")  # Разделительная линия
    print(result_operation.rjust(width).upper())  # Вывод результата


# Запрашиваем выбор системы счисления
base = int(input("Выберите систему счисления (2 - двоичная, 8 - восьмеричная, 10 - десятичная, 16 - шестнадцатеричная): "))

# Запрашиваем ввод чисел
num1_str = input(f"Введите первое число в системе счисления {base}: ")
num2_str = input(f"Введите второе число в системе счисления {base}: ")
operation = input("Выберите операцию (+, -, *, /): ")

if len(num1_str) < len(num2_str):
    num1_str, num2_str = num2_str, num1_str

# Выполняем умножение и выводим результат в столбик
print('\nРезультат: ')
if operation == '*':
    multiplication(num1_str, num2_str, base)
if operation == '-' or operation == '+':
    addition_and_subtraction(num1_str, num2_str, base, operation)
else:
    print('Неизвестная операция')
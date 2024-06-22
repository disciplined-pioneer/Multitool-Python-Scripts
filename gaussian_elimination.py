import numpy as np
from fractions import Fraction

# Запрос количества переменных
num_variables = int(input("Введите количество строк в матрице: "))

# Запрос коэффициентов системы
print("Введите коэффициенты матрицы:")
matrix = []
for i in range(num_variables):
    row = list(map(float, input(f"Введите коэффициенты для строки {i+1} (через пробел): ").split()))
    matrix.append(row)

matrix_users = np.array(matrix, dtype=float)

matrix1 = matrix_users.copy()
num_equations, num_columns = matrix1.shape
all_matrices = [matrix_users]
result_index = []

# Приведение к ступенчатому виду
for col in range(num_columns - 1):

    # Находим индекс строки с максимальным по модулю элементом в текущем столбце
    base_row = np.argmax([
        np.abs(matrix1[row, col]) if row not in result_index else -np.inf
        for row in range(matrix1.shape[0])
    ])
    result_index.append(base_row)

    # Проверка на случай, если элемент равен нулю
    if matrix1[base_row, col] == 0:
        continue

    # Обнуление всех остальных элементов в текущем столбце
    for row in range(num_equations):
        if row != base_row:
            # Находим коэффициент для вычитания
            coeff = matrix1[row, col] / matrix1[base_row, col]
            matrix1[row] -= coeff * matrix1[base_row]

    # Нормализуем базовую строку и сохраняем текущее состояние матрицы
    matrix1[base_row] /= matrix1[base_row, col]
    all_matrices.append(matrix1.copy())
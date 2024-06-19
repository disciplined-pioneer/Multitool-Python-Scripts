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
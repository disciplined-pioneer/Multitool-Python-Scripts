import numpy as np
from fractions import Fraction

def determinant(matrix):
    
    print('\nВычисление детерминанта: ')

    right_matrix = matrix[:, :2]
    matrix = np.hstack((matrix, right_matrix))
    
    rows, cols = matrix.shape
    result = 0

    # Проверка на минимальный размер матрицы
    if rows < 3 or cols < 5:
        raise ValueError("Матрица должна быть размером минимум 3x5.")

    # Перебор всех допустимых индексов, чтобы не выходить за границы матрицы
    for i in range(cols - 4):
        term1 = matrix[0, i] * matrix[1, i + 1] * matrix[2, i + 2]
        term2 = matrix[0, i + 1] * matrix[1, i + 2] * matrix[2, i + 3]
        term3 = matrix[0, i + 2] * matrix[1, i + 3] * matrix[2, i + 4]

        term4 = matrix[0, i + 2] * matrix[1, i + 1] * matrix[2, i]
        term5 = matrix[0, i + 3] * matrix[1, i + 2] * matrix[2, i + 1]
        term6 = matrix[0, i + 4] * matrix[1, i + 3] * matrix[2, i + 2]

        # Суммирование результата по формуле
        result += term1 + term2 + term3 - term4 - term5 - term6
        print(f"D = {term1} + {term2} + {term3} - {term4} - {term5 }- {term6} = {result}\n")
        print('-' * 30)

    return result

def main():

    # Запрос количества переменных
    num_variables = int(input("Введите количество строк в матрице: "))

    # Запрос коэффициентов системы
    print("Введите коэффициенты матрицы:")
    matrix = []
    for i in range(num_variables):
        row = list(map(float, input(f"Введите коэффициенты для строки {i+1} (через пробел): ").split()))
        matrix.append(row)

    matrix = np.array(matrix, dtype=float)

if __name__ == "__main__":
    main()
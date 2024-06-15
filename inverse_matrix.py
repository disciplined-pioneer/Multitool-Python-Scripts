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

def degree_minus_1(matrix):

    determ = determinant(matrix)
    
    if determ != 0:
        # Инициализация матрицы результатов
        matrix_result = np.zeros((3, 3))
        
        print("\nИсходная матрица:")
        print(matrix)
        print("\nВычисление значений A для каждой ячейки:\n")
        
        # Проход по каждой ячейке матрицы
        for row in range(3):
            for col in range(3):
                
                # Формируем матрицу миноров
                minors = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
                
                # Вычисляем произведения диагоналей
                main_diagonal = np.prod(np.diagonal(minors))
                secondary_diagonal = np.prod(np.diagonal(np.fliplr(minors)))
                
                A = main_diagonal - secondary_diagonal
                
                # Меняем знак в зависимости от положения
                if (row + col) % 2 != 0:
                    A = -A
                
                matrix_result[row, col] = A
                
                # Вывод промежуточных результатов
                print(f"A({row+1}, {col+1}):")
                print(minors)
                print(f"Главная диагональ: {main_diagonal}")
                print(f"Второстепенная диагональ: {secondary_diagonal}")
                print(f"Результат A({row+1}, {col+1}) = {A}\n")
        
        # Транспонирование и вычисление окончательного результата
        return  1 / determ * matrix_result.T

    else:
        return None

def print_result(matrix):
    print("Результат:")
    fraction_result = [[Fraction(elem).limit_denominator() for elem in row] for row in matrix]

    # Установим ширину для красивого выравнивания
    max_length = max(len(str(Fraction(elem).limit_denominator())) for row in fraction_result for elem in row)

    # Печатаем с отступом
    for row in fraction_result:
        print("   ".join(f"{str(elem):>{max_length}}" for elem in row))
    print()

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

    result = degree_minus_1(matrix)
    if result is None:
        print('D = 0. Решения не существует')
    else:
        print_result(result)

if __name__ == "__main__":
    main()
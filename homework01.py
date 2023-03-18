# Напишите функцию для транспонирования матрицы
# import numpy


def matrix_transpon(matrix: [[int]]) -> [[int]]:
    result_matrix = [[]]
    one_string = []
    result_matrix.clear()
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            one_string.append(matrix[j][i])
        result_matrix.append(list(one_string))
        one_string.clear()

    # matrix = numpy.array(matrix)
    # result_matrix = matrix.T
    return result_matrix


my_matrix = [[2, 3, 4], [5, 6, 7], [1, 1, 1], [0, 0, 0]]

print('Исходная матрица:')
for item in my_matrix:
    print(item)
print('Транспонированная матрица:')
for item in matrix_transpon(my_matrix):
    print(item)


# Напишите функцию для транспонирования матрицы


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = []
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row. append(matrix[i][j])
        transposed_matrix.append(transposed_row)

    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose(matrix)
print(transposed)

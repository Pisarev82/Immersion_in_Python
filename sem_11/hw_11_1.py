"""Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""


class Matrix:
    """Класс Матрица, который включает методы для вывода на печать, сравнения, сложения и умножения матриц."""

    def __init__(self, rows, columns):
        """Принимает количество строк и столбцов матрицы и создает пустую матрицу, заполнив ее нулями."""
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        """Переопределен для вывода матрицы в виде строк."""
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.data])

    def __eq__(self, other):
        """Два объекта матриц считаются равными, если они имеют одинаковые размеры и идентичные элементы."""
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.columns != other.columns:
            return False
        return self.data == other.data

    def __add__(self, other):
        """Проверяет, что слагаемое является объектом матрицы и имеет
        одинаковые размерности с текущей матрицей, а затем выполняет поэлементное сложение."""
        if not isinstance(other, Matrix):
            raise TypeError("Нельзя сложить НЕ Матрицу с матрицей")
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Нельзя сложить Матрицы разных размеров")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """ Если аргумент является матрицей, он проверяет, что количество столбцов
        текущей матрицы равно количеству строк аргумента, а затем выполняет стандартное матричное умножение.
        Если аргумент является числом, он умножает каждый элемент матрицы на это число."""
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("Нельзя перемножить Матрицы несовместимых размеров")
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        elif isinstance(other, int) or isinstance(other, float):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] * other
            return result
        else:
            raise TypeError("Нельзя умножать не числа")

# Создание и использование объектов класса Matrix
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]
print(matrix1)
# Выводит:
# 1 2
# 3 4

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]
print(matrix2)
# Выводит:
# 5 6
# 7 8

print(matrix1 == matrix2)  # Выводит: False

matrix3 = matrix1 + matrix2
print(matrix3)
# Выводит:
# 6 8
# 10 12

matrix4 = matrix1 * matrix3
print(matrix4)
# Выводит:
# 26 32
# 58 72

matrix5 = matrix1 * 2
print(matrix5)
# Выводит:
# 2 4
# 6 8
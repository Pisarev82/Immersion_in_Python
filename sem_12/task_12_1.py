"""Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k рассчитанных факториалов.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""
from math import factorial


class Factorial:

    def __init__(self, k):
        self.k = k
        self.last_factorial = []

    def __call__(self, n):
        result = factorial(n)
        self.last_factorial.append((n, result))
        self.last_factorial = self.last_factorial[-self.k:]
        return result

    def get_history(self):
        return self.last_factorial


if __name__ == '__main__':
    a = Factorial(5)
    for i in range(6):
        print(a(i))

    print(a.get_history())

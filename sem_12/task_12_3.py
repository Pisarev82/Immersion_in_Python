"""Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""

from math import factorial


class Factorial:

    def __init__(self, start=1, stop=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.first = 1
        self.second = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first * self.second
            if self.start <= self.first < self.stop:
                return self.first
            raise StopIteration



if __name__ == '__main__':
    a = Factorial(stop=1000000)
    for i in a:
        print(i)




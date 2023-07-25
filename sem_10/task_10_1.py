"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circle(self):
         return 2 * self.radius * math.pi

    def area_circle(self):
        return self.radius ** 2 * math.pi


a = Circle(5)
print(a.len_circle(), a.area_circle())

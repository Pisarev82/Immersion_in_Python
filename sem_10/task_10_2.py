"""Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, side_1, side_2= None):
        self.side_1 = side_1
        self.side_2 = side_2
        if not side_2:
            self.side_2 = side_1


    def perimetr(self):
        return (self.side_1 + self.side_2) * 2

    def aray_rectangle(self):
        return self.side_1 * self.side_2


a = Rectangle(5, 2)
print(Rectangle.aray_rectangle(a), a.perimetr())
b = Rectangle(5)
print(b.aray_rectangle(), b.perimetr())

"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения

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

    def __add__(self, other):
        p = (self.perimetr() + other.perimetr())
        return Rectangle( int(p / 4), int(p / 4))

    def __sub__(self, other):
        p_1, p_2 = self.perimetr(), other.perimetr()
        if p_1 < p_2:
            p_1, p_2 = p_2, p_1
        p = (p_1 - p_2)
        return Rectangle(int(p / 4), int(p / 4))

    def __eq__(self, other):
        return self.aray_rectangle() == other.aray_rectangle()

    def __lt__(self, other):
        return self.aray_rectangle() < other.aray_rectangle()

    def __le__(self, other):
        return self.aray_rectangle() <= other.aray_rectangle()

    def __ge__(self, other):
        return self.aray_rectangle() >= other.aray_rectangle()

    def __str__(self):
        return f"Прямоугольник со стороной {self.side_1} и {self.side_2}"

    def __repr__(self):
        return f"Rectangle(side_1 =  {self.side_1}, side_2 = {self.side_2 = })"


a = Rectangle(5, 2)
print(Rectangle.aray_rectangle(a), a.perimetr())
b = Rectangle(5)
print(b.aray_rectangle(), b.perimetr())
c = a + b
print(c.side_1, c.side_2)
c = a - b
print(c.side_1, c.side_2)
print(a > b, a != b)
print(c)
print(f"{c= }")
"""Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.

Задание №5
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    __slots__ = ('_side_1', '_side_2', '_c')

    def __init__(self, side_1, side_2= None):
        self._side_1 = side_1
        self._side_2 = side_2
        if not side_2:
            self._side_2 = side_1

    @property
    def side_1(self):
        return self._side_1

    @property
    def side_2(self):
        return self._side_2

    @side_1.setter
    def side_1(self, value):
        if value > 0:
            self._side_1 = value

    @side_2.setter
    def side_2(self, value):
        if value > 0:
            self._side_2 = value

    def perimetr(self):
        return (self._side_1 + self._side_2) * 2

    def aray_rectangle(self):
        return self._side_1 * self._side_2

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
        return f"Прямоугольник со стороной {self._side_1} и {self._side_2}"

    def __repr__(self):
        return f"Rectangle(side_1 =  {self._side_1}, side_2 = {self._side_2 })"


if __name__ == '__main__':
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
    c.side_1 = 4
    print(f"{c= }")

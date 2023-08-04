"""Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Range:
    def __init__(self, min_value: int = None):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value <= self.min_value:
            raise ValueError(f'Значение {value} должно быть больше 0')


class Rectangle:
    side_1 = Range(0)
    side_2 = Range(0)

    def __init__(self, side_1, side_2=None):
        self._side_1 = side_1
        self._side_2 = side_2
        if not side_2:
            self._side_2 = side_1

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
    c.side_1 = -1
    print(f"{c= }")

"""На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest


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


class TestCaseName(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Rectangle(5, 2)
        self.b = Rectangle(2, 5)

    def test_is_create(self):
        self.assertEqual(Rectangle(5, 2), self.a)

    def test_summ_create_2(self):
        self.assertGreaterEqual(Rectangle(5, 2), Rectangle(5, 2))

    def test_sum(self):
        self.assertEqual(self.a + self.b, Rectangle(7, 7))

    def test_sub(self):
        self.assertEqual(self.a - self.b, Rectangle(0, 0))

    def test_eqvals(self):
        self.assertTrue(self.a, self.b)

    def test_not_eqvals(self):
        self.assertFalse(self.a == Rectangle(1, 1))

    def test_perimetr(self):
        self.assertEqual(self.a.perimetr(), 14)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
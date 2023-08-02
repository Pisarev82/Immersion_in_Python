"""Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import unittest
from sem_14.task_14_1 import clear_text


class TestCaseName(unittest.TestCase):

    def test_1(self):
        self.assertEqual(clear_text("python"), "python")

    def test_2(self):
        self.assertEqual(clear_text("PyThon"), "python")

    def test_3(self):
        self.assertEqual(clear_text("python!"), "python")

    def test_4(self):
        self.assertEqual(clear_text("python змея"), "python ")

    def test_5(self):
        self.assertEqual(clear_text("pyThon - змея?"), "python  ")


if __name__ == '__main__':
    unittest.main()

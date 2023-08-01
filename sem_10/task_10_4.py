"""Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
import random
from task_10_3 import Human


class Staff(Human):
    MAGIK_NUM = 7
    x = 7

    def __init__(self, *args, **kwargs):
        self.id_num = random.randint(1, 1000000)
        self.level = self.set_level()
        super().__init__(*args, **kwargs)

    def set_level(self):
        return sum(map(int, str(self.id_num))) % self.MAGIK_NUM


if __name__ == "__mane__":
    p = Staff(age=1, surname="Писарев", name="Николай", patronymic="Иванович")
    print(p.level)


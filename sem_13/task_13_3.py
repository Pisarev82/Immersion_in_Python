"""Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class BaseExeption(Exception):
    pass


class LevelExeption(BaseExeption):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Вам не хватает доступа для регистрации уровня меньше {self.data}"


class AccessExeption(BaseExeption):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"{self.data} не найдено"

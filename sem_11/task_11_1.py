"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)

Добавьте к задачам 1 и 2 строки документации для классов.

"""
import time


class MyString(str):
    """Класс добавляет 2 свойства, дополнительную строку и время создания экземпляра."""

    def __new__(cls, value, author):
        obj = super().__new__(cls, value)
        obj.author = author
        obj.created_at = time.time()
        return obj

    def __str__(self):
        return f"{super.__str__(self)}, автор: {self.author}, создана: {self.created_at}"


if __name__ == '__main__':
    my_string = MyString("Hello, world!", "Kolya")
    my_string_1 = MyString("Hello, world!", "Vasya")
    print(my_string)
    print(my_string.author, my_string.created_at)
    print(my_string_1.author, my_string_1.created_at)
    print(my_string + my_string_1.upper())
    help(MyString)
    print(my_string)


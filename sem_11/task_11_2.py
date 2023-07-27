"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра

Добавьте к задачам 1 и 2 строки документации для классов.

Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.

"""


class Archive:
    """Класс только записывает в списки все значения экземпляров"""
    my_list_number = []
    my_list_string = []

    def __init__(self, number, string_):
        self.number = number
        self.string_ = string_
        self.my_list_number.append(number)
        self.my_list_string.append(string_)

    def __str__(self):
        return f"Экземляр с числом {self.number} и строкой {self.string_}"

    def __repr__(self):
        return f"Archive({self.number}, {self.string_})"


if __name__ == '__main__':
    a = Archive(1, "one")
    b = Archive(2, "To")
    print(Archive.my_list_number, Archive.my_list_string)
    help(Archive)
    print(b)
    print(f"{b= }")



"""Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""


class Human:
    def __init__(self, *,  age, surname, name, patronymic):
        self.__age = age
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def fulname(self):
        return f"{self.surname} {self.name} {self.patronymic}"

if __name__ == '__main__':
    human = Human(age=1, surname="Писарев", name="Николай", patronymic="Иванович")
    print(human.fulname())
    print(human.get_age())
    human.birthday()
    print(human.get_age())


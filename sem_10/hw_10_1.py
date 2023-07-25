"""Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""
from enum import Enum
from task_10_5 import *


class Factory:
    __factory_dict = {
        "Animal": Animal,
        "Fish": Fish,
        "Bird": Bird,
        "Mammals": Mammals
    }

    # @staticmethod
    def create_animal(self, animal_type, *args) -> Animal:
        return self.__factory_dict[animal_type](*args)


if __name__ == '__main__':
    factory = Factory()
    animal = factory.create_animal("Animal", "Животное", 1)
    bird = factory.create_animal("Bird", 15, "Птица", 1)
    fish = factory.create_animal("Fish", "Да", 5000, "Рыба", 1)
    mam = factory.create_animal("Mammals", "Да", "davg", 1)
    print(type(animal), type(bird), type(fish), type(mam))


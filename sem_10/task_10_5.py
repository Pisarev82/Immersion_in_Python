"""Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Animal:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animal):
    def __init__(self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        if self.fresh_water:
            return True
        return False

    def check_deep(self):
        if self.deep < 3:
            return "мелководная"
        elif self.deep < 100:
            return "среднеглубинная"
        return "глубоководная"


class Bird(Animal):
    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        return self.wingspan / 1.8


class Mammals(Animal):
    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return True
        return False


if __name__ == '__main__':
    a = Animal("Птица", 1)
    fish = Fish("Yes", 6, "weg", 1)
    print(fish.check_deep())
    bird = Bird(15, "Птица", 1)
    print(bird.specific())
    mammas = Mammals("No", "Mam", 1)
    print(mammas.specific())
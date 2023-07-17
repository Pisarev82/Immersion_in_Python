# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import choice, randint

MAX_LENGTH = 7
MIN_LENGTH = 4
VOWELS = ["e", "y", "i", "u", "o", "a"]
CONSONANT = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h",
             "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]


def pseudonyms(count_row, file_name):
    with open(file_name, "a", encoding="UTF-8") as file:
        for _ in range(0, count_row):
            name = []
            for _ in range(0, randint(MIN_LENGTH, MAX_LENGTH)):
                    name.append(choice(CONSONANT))
            if not len(name and VOWELS):
                name[randint(MIN_LENGTH, MAX_LENGTH)] = choice(VOWELS)
            file.write(''.join(name).title() + "\n")


if __name__ == '__main__':
    pseudonyms(15, "names.txt")

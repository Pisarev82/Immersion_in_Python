# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
MAX_NUMBER = 1000
MIN_NUMBER = -1000


def fills_random_int_and_float(count_row, file_name):
    with open(file_name, "a", encoding="UTF-8") as file:
        for _ in range(count_row):
            print(f"{randint(MIN_NUMBER, MAX_NUMBER)} | {uniform(MIN_NUMBER, MAX_NUMBER)}", file=file)


if __name__ == '__main__':
    fills_random_int_and_float(10, "fills_random_int_and_float.txt")

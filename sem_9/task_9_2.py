"""Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from functools import wraps
from random import randint


def make_game(func):
    @wraps(func)
    def wrapper(number, attempts):
        if not 0 < number < 101:
            number = randint(1, 100)
        if not 0 < attempts < 11:
            attempts = randint(1, 10)
        func(number, attempts)
    return wrapper


@make_game
def game(number, attempts):
    print(f"Я выбрал число. У вас есть {attempts} попыток угадать его. ")
    count = 0
    while count < attempts:
        guess = int(input("Какое число я загадал?: "))

        if guess == number:
            print(f"Вы угадали число загаданное число {number} за {count} попыток")
            break

        elif guess > number:
            print("Меньше!")
        else:
            print("Больше!")

        count += 1
    else:
        print(f"Попытки закончились. Я загадал {number}.")


if __name__ == '__main__':

    game(26, 10)

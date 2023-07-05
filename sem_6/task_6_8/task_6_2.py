# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random

__all__ = ["my_func"]

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10


def my_func(lower_limit, upper_limit, attempts):
    print("Я выбрал число от 0 до 1000. У вас есть 10 попыток угадать его. ")
    number = random.randint(lower_limit, upper_limit)
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
    print(f"Попытки закончились. Я загадал {number}.")


if __name__ == '__main__':
    my_func(LOWER_LIMIT, UPPER_LIMIT, attempts)

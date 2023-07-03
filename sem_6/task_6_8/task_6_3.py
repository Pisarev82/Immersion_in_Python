# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import random
import sys

__all__ = ["my_func"]


def my_func(lower_limit=0, upper_limit=1000, attempts=10):
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit
    number = random.randint(lower_limit, upper_limit)
    print(f"Я выбрал число от {lower_limit} до {upper_limit}. У вас есть {attempts} попыток угадать его. ")
    remaining_attempts = attempts
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


if __name__ == "__main__":
    my_func(*[int(i) for i in sys.argv if i.isdigit()])

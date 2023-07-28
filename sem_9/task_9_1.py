"""Создайте функцию-замыкание, которая принимает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def make_game(number, attempts):
    print(f"Я выбрал число. У вас есть {attempts} попыток угадать его. ")

    def game():
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
    return game


if __name__ == '__main__':

    res = make_game(26, 10)
    res()

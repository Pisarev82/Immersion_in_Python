"""Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def chek_int_or_float():
    while True:
        user_input = input("Введите число: ")
        try:
            return int(user_input)
        except ValueError as e:
            try:
                return float(user_input)
            except ValueError as e1:
                print("Введено не корректное значение")


if __name__ == '__main__':

    print(chek_int_or_float())

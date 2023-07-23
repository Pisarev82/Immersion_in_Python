"""Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл."""
import csv
import json
import os.path
import random
from functools import wraps


def solve_from_csv(file_name):
    def deco(func):
        @wraps(func)
        def wrapper(*args):
            if not os.path.exists(file_name):
                data = []
            else:
                with open(file_name, "r") as file:
                    data = []
                    res = csv.reader(file, delimiter=",")
                    for row in res:
                        a, b, c = int(row[0]), int(row[1]), int(row[2])
                        result = func(a, b, c)
                        data.append([(a, b, c), result])
            return data
        return wrapper
    return deco


def save_param_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = 'hw_9_1.json'
        result = func()
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(result, file, ensure_ascii=False, indent=1)
        return result

    return wrapper


@save_param_to_json
@solve_from_csv('random_numbers.csv')
def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    # Если дискриминант положительный, уравнение имеет два различных корня
    if discriminant > 0:
        root_1 = (-b + discriminant**0.5) / (2*a)
        root_2 = (-b - discriminant**0.5) / (2*a)
        print("Уравнение имеет два различных корня: x1 =", root_1, "и x2 =", root_2)
        return root_1, root_2

    # Если дискриминант равен нулю, уравнение имеет один корень
    elif discriminant == 0:
        root = -b / (2*a)
        print("Уравнение имеет один корень: x =", root)
        return root

    # Если дискриминант отрицательный, уравнение не имеет реальных корней
    else:
        print("Уравнение не имеет реальных корней")
        return None


def generate_random_to_csv(file_name):
    # Подготавливаем данные
    data = []
    for _ in range(100):
        row = [random.randint(1, 100) for _ in range(3)]
        data.append(row)

    # Записываем данные в CSV-файл
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


if __name__ == '__main__':
    generate_random_to_csv('random_numbers.csv')
    solve_quadratic_equation()

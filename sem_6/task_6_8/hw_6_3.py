# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random


def queens_beat(queens):
    # Проверяем, разделяет ли какой-либо ферзь одну и ту же строку или столбец
    for q1 in queens:
        x1, y1 = q1
        for q2 in queens:
            x2, y2 = q2
            if q1 != q2 and (x1 == x2 or y1 == y2):
                return False

    # Проверьте, имеет ли любой ферзь одну и ту же диагональ
    for q1 in queens:
        x1, y1 = q1
        for q2 in queens:
            x2, y2 = q2
            if q1 != q2 and abs(x1 - x2) == abs(y1 - y2):
                return False

    return True


# queens = []

# for _ in range(8):
#     x, y = map(int, input().split())
#     queens. append((x, y))
# print(queens)
# if queens_beat(queens):
#     print("Королевы НЕ бьют друг друга")
# else:
#     print("Королевы бьют друг друга")


def find_4_successful_formations():
    successful_formations = []
    num_formations = 0

    while num_formations < 4:
        queens = []
        for _ in range(8):
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            queens.append((x, y))
            print(queens)

        if queens_beat(queens):
            successful_formations.append(queens)
            num_formations += 1
            print(num_formations)

    print(successful_formations)

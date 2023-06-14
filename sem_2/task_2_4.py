# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# * Диаметр не превышает 1000 у.е.
# * Точность вычислений должна составлять
# не менее 42 знаков после запятой

import decimal
import math

while True:
    diam = int(input("Введите диаметр: "))
    if diam <= 1000:
        break

decimal.getcontext().prec = 42
square = decimal.Decimal(math.pi * diam * diam / 4)
leigth = decimal.Decimal(math.pi * diam)

print(f"Диаметр круа {diam} у.е. его площадь {square} квадратных у.е, а окружность {leigth} у.е.")

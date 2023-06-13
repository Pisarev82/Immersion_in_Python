# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import math
from fractions import Fraction

"""
Надеюсь я угадал с математикой. Выделение целой части не делал, потому что Fraction ее так же не выделяет.
по условиям задания не увидел запрета на использование модуля math для нахождения наибольшего общего делителя.
"""

num_1, den_1 = map(int, input("Ввидете дробь вида “a/b” без кавычек: ").split("/"))
num_2, den_2 = map(int, input("Ввидете дробь вида “a/b” без кавычек: ").split("/"))

if den_1 == den_2:
    sum_num = num_1 + num_2
    sum_den = den_1
else:
    sum_num = num_1 * den_2 + num_2 * den_1
    sum_den = den_1 * den_2

nod_1 = math.gcd(sum_num, sum_den)
sum_num /= nod_1
if nod_1 == sum_den:
    print(f"Сумма дробей: {int(sum_num)}")
else:
    sum_den /= nod_1
    print(f"Сумма дробей: {int(sum_num)}/{int(sum_den)}")
frac_sum = Fraction(num_1, den_1) + Fraction(num_2, den_2)
print("Проверка суммы ", frac_sum)

mult_num = num_1 * num_2
mult_den = den_1 * den_2

nod_1 = math.gcd(mult_num, mult_den)
mult_num /= nod_1
if nod_1 == mult_den:
    print(f"Произвдение дробей: {int(mult_num)}")
else:
    mult_den /= nod_1
    print(f"Произвдение дробей: {int(mult_num)}/{int(mult_den)}")
frac_mult = Fraction(num_1, den_1) * Fraction(num_2, den_2)
print("Проверка произвдения ", frac_mult)

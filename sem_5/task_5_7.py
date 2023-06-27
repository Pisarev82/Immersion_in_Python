# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def prime_numbers(n: int):
    count = 0
    check_number = 2
    while count != n:
        if all(check_number % y != 0 for y in range(2, check_number)):
            count += 1
            yield check_number
        check_number += 1


print(*prime_numbers(17))




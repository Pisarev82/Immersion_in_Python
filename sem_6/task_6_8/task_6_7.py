# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import sys

__all__ = ["validate_date", "term_validate_date"]


def validate_date(date_string):
    day, month, year = date_string.split('.')
    day, month, year = int(day), int(month), int(year)
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 9999:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2:
        if _is_leap_year(year):
            if day > 29:
                return False
        elif day > 28:
            return False
    return True


def _is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def term_validate_date():
    return validate_date(sys.argv[1])


if __name__ == '__main__':
    print(validate_date("01.02.23"))
    print(validate_date("29.02.4"))
    print(validate_date("29.02.5"))
    print(validate_date("29.02.10000"))
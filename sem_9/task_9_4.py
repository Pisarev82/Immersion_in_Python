"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции
"""
from functools import wraps


def repeater(count: int):
    def deco(func):
        @wraps(func)
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return deco


@repeater(5)
def any_func():
    print("Hello world")


if __name__ == '__main__':
    any_func()

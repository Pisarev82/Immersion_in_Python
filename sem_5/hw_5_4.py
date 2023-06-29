# Создайте функцию генератор чисел Фибоначчи

count_elems = 50


def fibonacci_generator(count_elems):
    first = 0
    second = 1
    yield 0
    count = 1
    while count_elems > count:
        first, second = second, first + second
        count += 1
        yield first


print(*fibonacci_generator(count_elems))


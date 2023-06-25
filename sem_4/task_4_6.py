# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# ✔ Для простоты будем использовать только положительную.
# индексацию

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
number_1, number_2 = map(int, input("Введите 2 числа через пробел: ").split(" "))


def sum_of_numbers (list_numbers, *args):
    index_1, index_2 = sorted(args)[0], sorted(args)[1]
    return sum(list_numbers[index_1:index_2])


print(sum_of_numbers(list_numbers, number_1, number_2))
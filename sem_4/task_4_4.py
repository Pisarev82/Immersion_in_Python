#Функция получает на вход список чисел.
#Отсортируйте список по убыванию суммы цифр

input_digits = [56, 36, 15, 0, 68, 45, 3, 2, 1, 5, 68, 15, 68, 10, 60]


def sum_numders(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits


print(sorted(input_digits, key=sum_numders, reverse=True))


def bubble_sort(lst):
    # Внимание, list является изменяемым объектом, таким образом измения происходят
    # во внутреннем списке lst и внешнем input_digits
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if sum_numders(lst[j]) > sum_numders(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]


bubble_sort(input_digits)
print(input_digits)

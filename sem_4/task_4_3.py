# * Функция получает на вход строку из двух чисел через пробел.
# * Сформируйте словарь, где ключом будет символ из Unicode,
# а значением — его порядковый номер из диапазона, границами которого являются введенные числа.
# * Границы диапазона учитывать.

text = "58 56"


def create_amaizing_dict(text: str) -> dict:
    limit_1, limit_2 = map(int, text.split(" "))
    if limit_2 < limit_1:
        limit_1, limit_2 = limit_2, limit_1
    result = {}
    for enum, i in enumerate(range(limit_1, limit_2 + 1), 1):
        result[chr(i)] = enum
    return result


print(create_amaizing_dict(text))

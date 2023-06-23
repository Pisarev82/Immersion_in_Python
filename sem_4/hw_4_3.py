# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def key_params_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            value = str(value)
        result[value] = key
    return result


result = key_params_dict(height=180, age=35, hobbies=['вяапр', 'чвпр'])
print(result)

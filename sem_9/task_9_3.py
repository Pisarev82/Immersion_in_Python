"""Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.

Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""
import json
import os.path
from functools import wraps


# data = {
#     'args': (*args, **kwargs),
#     'result': num
# }


def save_param_to_json(func):
    @wraps(func)
    def wrapper(num, *args, **kwargs):
        file_name = 'task_9_3.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf8') as file:
                res = json.load(file)
        else:
            res = []
        result = func(num, *args, **kwargs)
        res.append({
            'args': (num, args, kwargs),
            'result': result
                })
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(res, file, ensure_ascii=False, indent=1)
        return result

    return wrapper


@save_param_to_json
def get_any(num, *args, **kwargs):
    return num


if __name__ == '__main__':
    get_any(2, 15, 14, wqegf="qerf", ae="wrghw")

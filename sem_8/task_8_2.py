"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны в пределах уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import json
import os.path


def func(json_file):
    if os.path.isfile(json_file):
        with open("task_8_2.json", "r") as file:
            dict_ = json.load(file)
    else:
        dict_ = {str(i):{} for i in range(1, 8)}
    while True:
        user_input = input("Введите имя, идентификатор, уровень доступа: ")
        if not user_input:
            break
        name, id, level = user_input.split(" ")
        if id not in dict_[level]:
            dict_.setdefault(level, {id:name})[id] = name
    print(dict_)
    with open("task_8_2.json", "w") as file:
        json.dump(dict_, file, ensure_ascii=False)


if __name__ == '__main__':
    func("task_8_2.json")
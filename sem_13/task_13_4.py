"""Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Реализуйте магический метод проверки на равенство пользователей
"""
import json


class User:

    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f"Пользователь с id {self.user_id} имя {self.name} уровень доступа {self.level} \n"

    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.name}, level={self.level}) \n"

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name


def read_users_from_json(file_path):
    users_list = []
    with open(file_path, "r", encoding="utf8") as file:
        data = json.load(file)
    print(data)
    for level, users in data.items():
        for id_, name in users.items():
            users_list.append(User(id_, name, level))
    return users_list


if __name__ == '__main__':
    res = read_users_from_json("D:\\dev\\study\\Immersion _in_Python\\sem_8\\task_8_2.json")
    print(*res, end="\n")

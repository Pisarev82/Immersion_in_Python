"""Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
Класс имеет следующие методы:
Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
Метод входа в систему – требует указать имя и id пользователя.
Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
Если в списке его нет, то вызывается исключение доступа.
Если пользователь присутствует в списке пользователей проекта, то
пользователь, который входит получает его уровень доступа и становится администратором.
Метод добавление пользователя в список пользователей. Если уровень пользователя меньше,
чем ваш уровень, вызывайте исключение уровня доступа.
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта."""
import json

from sem_13.task_13_3 import AccessExeption, LevelExeption
from sem_13.task_13_4 import User


class Project:

    data = None

    def __init__(self, users_list: list, admin=None):
        self.users_list = users_list
        self.admin = admin

    @classmethod
    def load_from_json(cls, file_path):
        cls.__file_path = file_path
        with open(file_path, "r", encoding="utf8") as file:
            cls.data = json.load(file)
        users_list = []
        for level, users in cls.data.items():
            for id_, name in users.items():
                users_list.append(User(id_, name, level))
        return Project(users_list)

    def login_user(self):
        user_input = input("Введите Имя и id для входа ")
        name, id_ = user_input.strip().split(" ")
        user = User(id_, name, 0)
        if user not in self.users_list:
            AccessExeption(user)
        for each in self.users_list:
            if each == user:
                self.admin = each
                print("Вы вошли")

    def add_user(self):
        user_input = input("Для добавления нового пользователя введите имя, идентификатор, уровень доступа: ")
        name, id_, level = user_input.split(" ")
        if level < self.admin.level:
            raise LevelExeption(self.admin.level)
        if id_ not in self.data[level]:
            self.data.setdefault(level, {id_: name})[id_] = name

        with open(self.__file_path, "w", encoding="utf8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=1)

    def __str__(self):
        return f"{[user for user in self.users_list]}"

    def __repr__(self):
        return f"{[user for user in self.users_list]}"


if __name__ == '__main__':
    project = Project.load_from_json("D:\\dev\\study\\Immersion _in_Python\\sem_8\\task_8_2.json")
    print(project)
    project.login_user()
    print("+++ ", project.admin, project.admin)
    project.add_user()
    print("----", project)


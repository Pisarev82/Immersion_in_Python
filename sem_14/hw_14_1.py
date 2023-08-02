"""На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры."""
import pytest
from sem_13.task_13_3 import LevelExeption
from sem_13.task_13_4 import User
from sem_13.task_13_5 import Project


@pytest.fixture
def project(monkeypatch):
    # Создаем экземпляр проекта и настраиваем его для каждого теста
    users_list = [
        User('1', 'Alice', '4'),
        User('2', 'Bob', '4'),
        User('3', 'Charlie', '3')
    ]
    res = Project(users_list)
    monkeypatch.setattr('builtins.input', lambda _: 'Alice 1')
    res.login_user()
    return res


def test_login_user(project, monkeypatch):
    # Изза того что метод внутри себя запрашивает ввод из консоли,
    # пришлось нагуглить monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: 'Bob 2')
    project.login_user()
    assert project.admin.level == '4'


def test_add_user(project, monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: 'Dave 5 6')
    project.add_user()
    assert len(project.users_list) == 4


def test_add_user_with_low_level(project, monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: 'Eve 10 1')
    with pytest.raises(LevelExeption):
        project.add_user()


if __name__ == '__main__':
    pytest.main(['-v'])

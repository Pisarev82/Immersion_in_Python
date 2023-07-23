"""Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""


from sem_9.task_9_2 import game
from sem_9.task_9_2 import make_game
from sem_9.task_9_4 import repeater
from sem_9.task_9_3 import save_param_to_json



@repeater(2)
@save_param_to_json
@make_game
def func(number, attempts):
    game(number, attempts)


if __name__ == '__main__':
    func(10, 2)

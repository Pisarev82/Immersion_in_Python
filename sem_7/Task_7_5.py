# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import random

from task_7_4_and_7_6 import create_b_files


# def create_b_files_pro(*args, numb_files=1):
#     file_extensions = args
#
#     for _ in range(numb_files):
#         print(random.choice(file_extensions))
#         create_b_files(random.choice(file_extensions), numb_files=1)


def create_b_files_pro(**kwargs):
    for file_extension, numb_files in kwargs.items():
        create_b_files(file_extension, numb_files=numb_files)


if __name__ == '__main__':
    create_b_files_pro(txt=4, ttt=1, xxx=3, png=2, mp4=2)

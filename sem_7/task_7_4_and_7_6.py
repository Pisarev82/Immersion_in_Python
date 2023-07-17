"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


import os
import random
import string


def create_b_files(file_extension: str,
                   min_name_len=6, max_name_len=30,
                   min_file_len=256, max_file_len=4096,
                   *, numb_files=2,
                   file_storagedir="task_7_4"):
    # Проверяем существует ли папка для записи файлов, если нет создаем
    if not os.path.isdir(file_storagedir) and os.path.basename(os.getcwd()) != file_storagedir:
        curent_dir = os.getcwd()
        os.mkdir(curent_dir + "\\" + file_storagedir)
    if os.path.basename(os.getcwd()) != file_storagedir:
        os.chdir(file_storagedir)

    #Создаем указанное колличество файлов согласно условиям задачи
    for _ in range(numb_files):
        file_name_len = random.randint(min_name_len, max_name_len)
        file_name = "".join(random.choices(string.ascii_letters + string.digits, k=file_name_len)) + "." + file_extension
        file_len = random.randint(min_file_len, max_file_len)
        random_bytes = os.urandom(file_len)
        if not os.path.isfile(file_name):
            with open(file_name, "wb") as file:
                file.write(random_bytes)


if __name__ == '__main__':
    create_b_files("txt")
"""
Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.

* При переименовании в конце имени добавляется порядковый номер.

* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.

* принимать в качестве аргумента расширение конечного файла.
"""
import os
from os.path import join, isfile, isdir

DIR = join(os.getcwd(), "task_7_4")


def group_rename_files(new_name,
                       extention_for_work,
                       new_extention, dir):
    count = 1
    for file in os.listdir(dir):
        if isfile(join(dir, file)):
            if file.split(".")[1] == extention_for_work:
                new_full_name = f'{file.split(".")[0]}_{new_name}_{count}.{new_extention}'
                os.rename(join(dir, file), join(dir, new_full_name))
                count += 1
        elif isdir(join(dir, file)):
            group_rename_files(new_name, extention_for_work, new_extention, join(dir, file))



if __name__ == '__main__':
    group_rename_files("new", "ttt", "new", DIR)

"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
from os import listdir, getcwd, replace
from os.path import isfile, join, exists

DIR = join(getcwd(), "task_7_4")
EXTENSION_TYPES = {
    "Video": ("mkv", "avi", "mp4"),
    "Pict": ("png", "jpg", "jpeg"),
    "Text": ("txt", "bin"),
}


def group_by_file_extension(file_storage_dir=DIR):
    only_files = [f for f in listdir(file_storage_dir) if isfile(join(file_storage_dir, f))]
    for file in only_files:
        file_extension = file.split(".")[1]
        for item in EXTENSION_TYPES.items():
            if file_extension in item[1]:
                if not exists(join(DIR, item[0])):
                    os.mkdir(join(DIR, item[0]))
                replace(join(DIR, file), join(DIR, item[0], file))


if __name__ == '__main__':
    group_by_file_extension(join(getcwd(), "task_7_4"))


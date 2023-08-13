"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""
import os
from collections import namedtuple
import logging

FORMAT = '{msg}'
logging.basicConfig(filename='log/log_hw_1.log.',  level=logging.INFO,
                    format=FORMAT, style="{", encoding='utf-8')
logger = logging.getLogger(__name__)


def my_func(directory):
    Unit = namedtuple('Unit', ['file_name', 'file_expansion', 'parent_directory'])

    data = [Unit(os.path.basename(directory), 'dir', os.path.basename(directory))]
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            temp_dir = Unit(dirname, 'dir', os.path.basename(dirpath))
            data.append(temp_dir)
            logger.info(temp_dir)
        for filename in filenames:
            if len(filename.split('.')) == 2:
                file_name, file_expansion = filename.split('.')
            else:
                file_name, file_expansion = filename, 'file'

            temp_file = Unit(file_name, file_expansion, os.path.basename(dirpath))
            data.append(temp_file)
            logger.info(temp_file)


if __name__ == '__main__':
    my_func("D:\\dev\\study\\Immersion _in_Python\\sem_15")
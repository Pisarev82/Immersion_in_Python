"""Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import pickle


def convert_pickle_to_csv(pickle_file, csv_file):
    with (open(pickle_file, "rb") as file,
          open(csv_file, "w", newline="") as csv_file):
        data = pickle.load(file)
        print(data)
        keys = data[0].keys()
        print(keys)
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    convert_pickle_to_csv("task_8_4.pickle", "task_8_6.csv")

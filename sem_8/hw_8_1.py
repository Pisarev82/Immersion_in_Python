"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import csv
import json
import os
import pickle


def get_directory_size(directory):
    total_size = 0
    data = {os.path.basename(directory): {"size": 0,
                                          "Родитель": os.path.basename(directory),
                                          "Тип": "Папка"}}
    # Рекурсивный обход директорий
    for dirpath, dirnames, filenames in os.walk(directory):
        size = 0
        for dirname in dirnames:
            data[dirname] = {"size": 0,
                             "Родитель": os.path.basename(dirpath),
                             "Тип": "Папка"
                             }
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size += os.path.getsize(file_path)
            data[filename] = ({"size": os.path.getsize(file_path),
                               "Родитель": os.path.basename(dirpath),
                               "Тип": "Файл"})
            data[os.path.basename(dirpath)]["size"] = size
        total_size += size
    data[os.path.basename(directory)]["size"] = total_size

    # Сохранение результатов в json
    with open('hw_8_1.json', 'w', encoding="utf8") as json_file:
        json.dump(data, json_file, indent=1, ensure_ascii=False)
        json_file.write('\n')

    # Сохранение результатов в csv
    with open('hw_8_1.csv', 'w', newline="", encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Название", "size", "Родитель", "Тип"])
        writer.writeheader()
        for key, value in data.items():
            size = value["size"]
            parent = value["Родитель"]
            type_ = value["Тип"]
            writer.writerow({"Название": key,
                             "size": size,
                            "Родитель": parent,
                            "Тип": type_},
                            )

    # Сохранение результатов в pickle
    with open('hw_8_1.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == '__main__':
    get_directory_size("D:\dev\study\Immersion _in_Python\sem_7")

    with open('hw_8_1.pickle', 'rb') as pickle_file:
        res = pickle.load(pickle_file)
    print(f"{res= }")

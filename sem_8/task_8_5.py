"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import os
import pickle


def convert_json_to_pickle(dir_name):
    files_names = os.listdir(dir_name)
    json_files = [i for i in files_names if i.endswith(".json")]
    for file in json_files:
        print(file)
        with (open(file, "r") as input_file,
              open(file.strip(".json") + ".pickle", "wb") as output_file):
            data = json.load(input_file)
            pickle.dump(data, output_file)


if __name__ == '__main__':
    convert_json_to_pickle("D:\dev\study\Immersion _in_Python\sem_8")
    with open("task_8_2.pickle", "rb") as file:
        print(pickle.load(file))

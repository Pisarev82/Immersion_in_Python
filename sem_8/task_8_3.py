"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import csv
import json


def save_to_csv(input_file_name, output_file_name):
    with open(input_file_name, "r") as input_file:
        data = [["level", "id", "name"]]
        for level, value in json.load(input_file).items():
            for id_, name in value.items():
                data.append([level, id_, name])

    with open(output_file_name, "w", newline="") as file:
        csv_writer = csv.writer(file)
        for each in data:
            csv_writer.writerow(each)


if __name__ == '__main__':
    save_to_csv("task_8_2.json", "task_8_3.csv")

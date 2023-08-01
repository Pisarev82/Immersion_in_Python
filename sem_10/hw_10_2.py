"""Возьмите любую из задач с прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""
import csv
import json


class SaveToCsv:
    def __init__(self, input_file_name, output_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def save_to_csv(self):
        with open(self.input_file_name, "r") as input_file:
            data = [["level", "id", "name"]]
            for level, value in json.load(input_file).items():
                for id_, name in value.items():
                    data.append([level, id_, name])

        with open(self.output_file_name, "w", newline="") as file:
            csv_writer = csv.writer(file)
            for each in data:
                csv_writer.writerow(each)


if __name__ == '__main__':
    save_to_csv = SaveToCsv("D:\\dev\\study\\Immersion _in_Python\\sem_8\\task_8_2.json",
                "hw_10_2.csv")
    save_to_csv.save_to_csv()

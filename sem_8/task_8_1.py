"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json

dir = "D:\\dev\\study\\Immersion _in_Python\\sem_7\\result_task_7_3.txt"
data = []

def read_from_file_save_to_json(dir):
    with open(dir, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, number = line.strip().split(" ")
            name = name.title()
            number = float(number)
            data.append((name, number))
    with open("result_task_8_1", "w", encoding="utf8") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    read_from_file_save_to_json(dir)
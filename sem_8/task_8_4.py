"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import json


def csv_reader(input_file_name):
    with open(input_file_name, "r") as file:
        res = file.readlines()
    return res


def convert_data(data):
    list_res = []
    level_name, id_name, name_name = data[0].strip().split(",")
    for each in data[1:]:
        level, id_, name = each.strip().split(",")
        id_ = ("000000000" + id_)[-10:]
        name = name.title()
        list_res.append({level_name: level, id_name: id_, name_name: name, "hash": hash(name + id_)})
    return list_res


def save_to_json(input_file_name, output_file_name):
    input_data = csv_reader(input_file_name)
    result_data = convert_data(input_data)
    print(result_data)
    with open(output_file_name, "w") as file:
        json.dump(result_data, file, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    save_to_json("task_8_3.csv", "task_8_4.json")

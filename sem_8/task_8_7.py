"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку."""
import pickle


def csv_reader(input_file_name):
    with open(input_file_name, "r") as file:
        res = file.readlines()
    return res


def print_pickle_string(data):
    print(pickle.dumps(data))


if __name__ == '__main__':
    print_pickle_string(csv_reader("task_8_6.csv"))

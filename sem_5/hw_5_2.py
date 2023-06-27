# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path = "C:\\Users\\Николай\\Downloads\\2023-06-02_15-49-09.png"
# test = input("Input path: ")


def pars_absolute_path(path: str):
    name, extension = path.split("\\")[-1].split(".")
    return path, name, extension


print(pars_absolute_path(path))
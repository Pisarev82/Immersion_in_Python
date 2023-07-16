#  Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

FILE_NAMES = ["fills_random_int_and_float.txt", "names.txt", "result_task_7_3.txt"]


def open_files(file_names: list):

    with (
            open(file_names[0], "r", encoding="UTF-8") as numbers,
            open(file_names[1], "r", encoding="UTF-8") as names,
            open(file_names[2], "w", encoding="UTF-8") as result
    ):
        if count_lines(names, numbers):
            for name in names:
                number = numbers.readline()
                if not number.endswith('\n'):
                    numbers.seek(0)
                    number = numbers.readline()
                result.write(_logic(name.strip(), number))
        else:
            for number in numbers:
                name = names.readline()
                if not name.endswith('\n'):
                    names.seek(0)
                    name = names.readline()
                result.write(_logic(name.strip(), number))


def _logic(name: str, number: str):

    a, b = map(float, number.split("|"))
    product = a * b
    if product > 0:
        return f"{name.upper()} {int(round(product, 0))} \n"
    else:
        return f"{name.lower()} {abs(product)} \n"


def count_lines(file_1, file_2):
    file_1_line_count = sum(chunk.count('\n')
                   for chunk in iter(lambda: file_1.read(), ''))
    file_2_line_count = sum(chunk.count('\n')
                            for chunk in iter(lambda: file_2.read(), ''))
    file_1.seek(0)
    file_2.seek(0)
    if file_1_line_count > file_2_line_count:
        return True
    else:
        return False


if __name__ == '__main__':
    open_files(FILE_NAMES)

# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


s = 5
names = "names"
var_3 = "s"
var_4 = "Коля"
items = ("2names", "we4")
var_6 = "3names"


def magick():
    variables = list(filter(lambda x: not x[0].startswith("__"), globals().items()))
    for each in variables:
        if len(each[0]) > 1 and each[0][-1::] == "s":
            globals().setdefault(each[0][:-1], each[1])
            globals()[each[0]] = None


magick()
print(list(filter(lambda x: not x[0].startswith("__"), globals().items())))
print(names)
print(name)


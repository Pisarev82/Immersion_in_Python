# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


text = "Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки."
# text = input("Введите строку текста: ")

def printing_text(text: str):
    output_text = ""
    for char in text:
        if char.isalpha() or char == ' ':
            output_text += char

    text_list = sorted(output_text.split())
    max_len_word = len(max(text_list, key=len)) + 1
    for enumer, each in enumerate(text_list, 1):
        print(f"{enumer}{each:>{max_len_word}}")


printing_text(text)
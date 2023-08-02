"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
import string


def clean_text(text: str):
    text = text.lower()
    clear_text = (char for char in text if 96 < ord(char) < 123 or ord(char) == 32)
    return ''.join(clear_text)


def clear_text(text: str):
    text = text.lower()
    return ''.join((i for i in text if i in string.ascii_lowercase + ' '))


if __name__ == '__main__':
    print(clean_text("a z3514wrsGSR 345wr"))
    print(clear_text("a z3514wrsGSR 345wr"))

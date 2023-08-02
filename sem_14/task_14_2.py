"""Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


import string


def clean_text(text: str):
    text = text.lower()
    clear_text = (char for char in text if 96 < ord(char) < 123 or ord(char) == 32)
    return ''.join(clear_text)


def clear_text(text: str):
    """
    >>> clear_text('python')
    'python'
    >>> clear_text('PyThon')
    'python'
    >>> clear_text('python!')
    'python'
    >>> clear_text('python змея')
    'python '
    >>> clear_text('pyThon - змея?')
    'python  '
    """
    text = text.lower()
    return ''.join((i for i in text if i in string.ascii_lowercase + ' '))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

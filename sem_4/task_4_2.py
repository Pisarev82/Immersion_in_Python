# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = "Напишите функцию, которая принимает строку текста."

def to_sorted_unicode(text: str) -> list:
    char_list = set([ord(char) for char in text])
    result = sorted(char_list, reverse=True)
    return list(result)

print(to_sorted_unicode(text))
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input("Введите целое число: "))
print(hex(num))
hex_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
hex_digits = []
while num > 0:
    remainder = num % 16
    if remainder >= 10:
        hex_digits.append(hex_map[remainder])
    else:
        hex_digits.append(str(remainder))
    num //= 16
hex_digits.reverse()
print(f"0x{''.join(hex_digits)}")


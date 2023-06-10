# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число

user_input = None

while True:
    user_input = int(input("Введите число от 1 до 999: "))
    if 0 <= user_input < 1000:
        break

def strange_logic (user_input):
    if 0 <= user_input < 10:
        return user_input ** 2
    elif 10 <= user_input < 100:
        tens_digit = user_input // 10
        ones_digit = user_input % 10
        return tens_digit * ones_digit
    else:
        string_num = str(user_input)
        hundreds_digit = int(string_num[0])
        tens_digit = int(string_num[1])
        ones_digit = int(string_num[2])
        return ones_digit * 100 + tens_digit * 10 + hundreds_digit

print(strange_logic(user_input))
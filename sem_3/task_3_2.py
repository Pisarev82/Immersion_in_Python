# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# * Целое положительное число
# * Вещественное положительное или отрицательное число
# * Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# * Строку в нижнем регистре в остальных случаях

user_input = input("Введите что-нибудь: ")

if user_input.isdecimal() and "-" not in user_input:
    num = int(user_input)
    print(num)
elif "." in user_input and user_input.count(".") == 1:
    user_input_list = user_input.split(".")
    if len(user_input_list) == 2 and user_input_list[0].isdecimal() and user_input_list[1].isdecimal():
        print("er")
        dec = float(user_input)
        print(dec)
elif user_input.upper():
    user_input_lower = user_input.lower()
    print(user_input_lower)
else:
    # Остальные случаи в верхний регистр, думаю в задании действительно опечатка
    user_input_upper = user_input.upper()
    print(user_input_upper)



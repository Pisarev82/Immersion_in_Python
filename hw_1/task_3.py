# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def user_input_with_verification(text_to_user) -> int:
    while True:
        user_input = input(text_to_user)
        try:
            result = int(user_input)
        except:
            print("введенные данные не являются целым числом")
            continue
        if 100000 > result > 0:
            return result
        else:
            print("Введено число больше 100 000, попробуйте еще раз")

num = user_input_with_verification("Введите целое положительное число меньше 100 000: ")

if num < 2:
    print("По определению, 0 и 1 не являются ни простыми, ни составными.")
elif num == 2:
    print("2 - единственное четное простое число. ")
else:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} - простое число.")
    else:
        print(f"{num} - составное число.")
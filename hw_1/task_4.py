# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.\
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

import random

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10
remaining_attempts = attempts

number = random.randint(LOWER_LIMIT, UPPER_LIMIT)

print("Я выбрал число от 0 до 1000. У вас есть 10 попыток угадать его. ")


while remaining_attempts > 0:
    guess = int(input("Какое число я загадал?: "))

    if guess == number:
        print(f"Вы угадали число загаданное число {number} за {attempts-remaining_attempts} попыток")
        break

    elif guess > number:
        print("Меньше!")
    else:
        print("Больше!")

    remaining_attempts -= 1
if remaining_attempts == 0:
    print(f"Попытки закончились. Я загадал {number}.")
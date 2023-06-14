# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

"""
match - case получился перегружен ветвлениями.
Я бы вывел ветвления в отдельные функции, но тогда получается что функции используются только 1 или 2 раза.
Кроме того появляется проблемма с использованием глобальных переменных.
По этому оставил все ветвления в case.
Думаю при использовании ООП можно будет написать более читаемый код.
"""

total = 0
multiplicity = 50
wealth_tax = 0.1
pop_percent = 0.015
max_pop = 600
min_pop = 30
count = 0
bonus_count = 3
threshold_of_wealth_tax = 5_000_000
bonus_percetnt = 0.03


while True:
    choice = input("Допустимые действия: пополнить - 1, снять - 2, выйти - 3: ")

    if total > threshold_of_wealth_tax:
        wealth_tax_pay = int(round(total * wealth_tax, 0))
        total -= wealth_tax_pay
        print("Удержан налог на богатсво ", wealth_tax_pay)

    match choice:
        case "1":  # введено одно слово "1" пополнеие
            temp = int(input(f"Введите сумму кратную {multiplicity}: "))
            if temp % multiplicity == 0:
                total += temp
                count += 1
            else:
                print(f"Введенная сумма не кратна {multiplicity}")
                continue
            if count % bonus_count == 0:
                bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
                total += bonus_percetnt_payd
                print("Начислены проценты ", bonus_percetnt_payd)
        case "2":  # введено одно слово "2" снятие
            temp_user_input = int(input(f"Введите сумму кратную {multiplicity}: "))
            if temp_user_input % multiplicity != 0:
                print(f"Введенная сумма не кратна {multiplicity}")
                continue
            pop_money_percents_payd = round(temp_user_input * pop_percent, 0)
            if pop_money_percents_payd >= max_pop:
                pop_money_percents_payd = max_pop
            elif pop_money_percents_payd < min_pop:
                pop_money_percents_payd = min_pop
            temp = total - temp_user_input - pop_money_percents_payd
            if temp > 0:
                total = temp
                print("Удержанно ", pop_money_percents_payd, "Выдано ", temp_user_input)
                count += 1
            else:
                print("Недостаточно средств на снятие и коммисию за снятие")
            if count % bonus_count == 0:
                bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
                total += bonus_percetnt_payd
                print("Начислены проценты ", bonus_percetnt_payd)
        case "3":  # введено одно слово "3" выход
            print("Баланс", total)
            break
        case _:  # Аналогично default в других языках, ошибочные вводы
            print("Баланс", total)
            continue
    print("Баланс", total)

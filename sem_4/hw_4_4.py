# Возьмите задачу о банкомате из семинара 2.
# Разбейте код на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

#
# total = 0
# multiplicity = 50
# wealth_tax = 0.1
# pop_percent = 0.015
# max_pop = 600
# min_pop = 30
# count = 0
# bonus_count = 3
# threshold_of_wealth_tax = 5_000_000
# bonus_percetnt = 0.03
#
#
# def pay_wealth_tax(total: int) -> int:
#     if total > threshold_of_wealth_tax:
#         wealth_tax_pay = int(round(total * wealth_tax, 0))
#         total -= wealth_tax_pay
#         print("Удержан налог на богатсво ", wealth_tax_pay)
#         return total
#
#
# while True:
#     choice = input("Допустимые действия: пополнить - 1, снять - 2, выйти - 3: ")
#
#     total = pay_wealth_tax()
#
#     match choice:
#         case "1":  # введено одно слово "1" пополнеие
#             temp = int(input(f"Введите сумму кратную {multiplicity}: "))
#             if temp % multiplicity == 0:
#                 total += temp
#                 count += 1
#             else:
#                 print(f"Введенная сумма не кратна {multiplicity}")
#                 continue
#             if count % bonus_count == 0:
#                 bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
#                 total += bonus_percetnt_payd
#                 print("Начислены проценты ", bonus_percetnt_payd)
#         case "2":  # введено одно слово "2" снятие
#             temp_user_input = int(input(f"Введите сумму кратную {multiplicity}: "))
#             if temp_user_input % multiplicity != 0:
#                 print(f"Введенная сумма не кратна {multiplicity}")
#                 continue
#             pop_money_percents_payd = round(temp_user_input * pop_percent, 0)
#             if pop_money_percents_payd >= max_pop:
#                 pop_money_percents_payd = max_pop
#             elif pop_money_percents_payd < min_pop:
#                 pop_money_percents_payd = min_pop
#             temp = total - temp_user_input - pop_money_percents_payd
#             if temp > 0:
#                 total = temp
#                 print("Удержанно ", pop_money_percents_payd, "Выдано ", temp_user_input)
#                 count += 1
#             else:
#                 print("Недостаточно средств на снятие и коммисию за снятие")
#             if count % bonus_count == 0:
#                 bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
#                 total += bonus_percetnt_payd
#                 print("Начислены проценты ", bonus_percetnt_payd)
#         case "3":  # введено одно слово "3" выход
#             print("Баланс", total)
#             break
#         case _:  # Аналогично default в других языках, ошибочные вводы
#             print("Баланс", total)
#             continue
#     print("Баланс", total)

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
transaction_history = []


def pay_wealth_tax(total: int) -> int:
    if total > threshold_of_wealth_tax:
        wealth_tax_pay = int(round(total * wealth_tax, 0))
        total -= wealth_tax_pay
        print("Налог на богатство ", wealth_tax_pay)
    return total


def deposit(total: int) -> int:
    temp = int(input(f"Введите сумму, кратную {multiplicity}: "))
    if temp % multiplicity == 0:
        total += temp
        transaction_history.append(('Вклад ', temp))
        print("Пополнение успешно баланс", total)
        return total
    else:
        print(f"Введенная сумма не кратна {multiplicity}")
        return total


def withdraw(total: int) -> int:
    temp_user_input = int(input(f"Введите сумму, кратную {multiplicity}: "))
    if temp_user_input % multiplicity != 0:
        print(f"Введенная сумма не кратна {multiplicity}")
        return total
    pop_money_percents_payd = round(temp_user_input * pop_percent, 0)
    if pop_money_percents_payd >= max_pop:
        pop_money_percents_payd = max_pop
    elif pop_money_percents_payd < min_pop:
        pop_money_percents_payd = min_pop

    temp = total - temp_user_input - pop_money_percents_payd
    if temp > 0:
        total = temp
        transaction_history.append(('Снятие ', temp_user_input))
        print("Снятие успешно баланс", total)
    else:
        print("Не хватает средст на вашем счету для снятия и процентов")
    return total

while True:
    choice = input("Допустимые действия: пополнить - 1, снять - 2, выйти - 3: ")
    total = pay_wealth_tax(total)

    match choice:
        case "1":
            total = deposit(total)
            count += 1
            if count % bonus_count == 0:
                bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
                total += bonus_percetnt_payd
                transaction_history.append(('проценты', bonus_percetnt_payd))
                print("Начисленны проценты ", bonus_percetnt_payd)
        case "2":
            total = withdraw(total)
            count += 1
            if count % bonus_count == 0:
                bonus_percetnt_payd = int(round(total * bonus_percetnt, 0))
                total += bonus_percetnt_payd
                transaction_history.append(('проценты', bonus_percetnt_payd))
                print("Списаны проценты ", bonus_percetnt_payd)
        case "3":
            print("Баланс: ", total)
            print("История операций:", transaction_history)
            break
        case _:
            print("Не верный ввод. Попробуйте еще. ")
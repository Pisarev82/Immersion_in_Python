# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

names = ["Иван", "Коля", "Петя", "Вася"]
salarys = [10000, 11000, 15000, 20000]
percents = ['10.25%', '15.00%', '20%', '25.25%']

def salary_bonus(names, salarys, percents):
    bonus_in_cash = [salary * float(bonus.strip("%")) / 100
                     for salary in salarys
                     for bonus in percents]
    return dict(zip(names, bonus_in_cash))


print(salary_bonus(names, salarys, percents))

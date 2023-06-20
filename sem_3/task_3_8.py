#  Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

camping_stuff = {"Коля": ("Кружка", "Ложка", "Мясо", "Зажигалка", "Вода", "Газировка", "Гитара"),
                 "Вася": ("Кружка", "Мясо", "Вода", "Пиво", "Газета", "Уголь", "Спички"),
                 "Петя": ("Кружка", "Топор", "Вода", "Спички", "Гитара", "Лежак", "Мясо",),
                 "Валя": ("Кружка", "Зеркало", "Вода", "Спички", "Салфетки", "Чайник", "Гитара"),
                 }

all_things = set.union(*[set(camping_stuff[friend]) for friend in camping_stuff])

# пример работы пересечения set.intersection для 3 множеств.
# all_things = set.intersection(set(camping_stuff["Коля"]), set(camping_stuff["Вася"]), set(camping_stuff["Петя"]),)
#Используя list comprehension можем обрабатывать вещи любого колличества друзей.
Everyone_things = set.intersection(*[set(camping_stuff[friend]) for friend in camping_stuff])
print("Cледующие вещи есть у каждого:", ", ".join(Everyone_things))

unique_things = set.union(*[set(camping_stuff[friend]) for friend in camping_stuff]) - Everyone_things
print("Вещи, которые принес только один друг:", ', '.join(unique_things))

missing_things = {thing: [] for thing in all_things}
for friend, things in camping_stuff.items():
    for thing in all_things:
        if thing in things:
            missing_things[thing].append(friend)
print("Вещи, которые есть у всех друзей, кроме одного:")
for thing, friends_missing in missing_things.items():
    if len(friends_missing) == len(camping_stuff) - 1:
        friend_missing = set(camping_stuff.keys()) - set(friends_missing)
        print(f"\t{thing} нет у: {friend_missing.pop()}")





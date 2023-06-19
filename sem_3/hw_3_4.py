# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
capacity = 10
items = {
 'вода': 1.5,
 'еда': 2.0,
 'тент': 3.5,
 'спальный мешок': 2.5,
 'плита': 1.0,
 'набор посуды': 1.5,
 'одежда': 2.0,
 'аптечка': 1.0,
 'топор': 1.75,
}


def get_combinations(dic):
    # базовый случай, выход из рекурсии: когда больше не осталось значений для добавления
    if not dic:
        return [[]]

    # рекурсивный случай: добавить первую пару ключ-значение в комбинации
    key, value = dic.popitem()
    subsets = get_combinations(dic)

    # создаем новые комбинации, включая или исключая текущую пару ключ-значение
    new_subsets = [subset + [(key, value)] for subset in subsets] + subsets

    return new_subsets

# находим все возможные комбинации
all_combinations = get_combinations(items.copy())

# Откладываем в отдельный список комбинации, вес которых равен максимальной вместимости.
true_combinations = []
for combination in all_combinations:
    if sum([value[1] for value in combination]) == capacity:
        true_combinations.append(combination)

# печатаем результат
for combination in true_combinations:
    print(*combination)

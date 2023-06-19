# * Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который
# содержит уникальные (без повтора) элементы исходного списка.
#
#
# * Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
listik = []
for item in range(10):
    listik.append(item)
    listik.append(item)

print(listik)

new_list = list(set(listik))
print(type(new_list), new_list)

new_list_2 = []
for item in listik:
    if item not in new_list_2:
        new_list_2.append(item)

print(type(new_list_2), new_list_2)
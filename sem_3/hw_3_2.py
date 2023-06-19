# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

listik  = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 1, 2, 1]

repit_in_listik = []
unique_list = []
for each in listik:
    if each not in unique_list:
        unique_list.append(each)
    else: repit_in_listik.append(each)

print(list(set(repit_in_listik)))



# * Создайте вручную список с повторяющимися элементами.
# * Удалите из него все элементы, которые встречаются дважды.

listik = [1, 1, 1, 2, 8, 2, 3, 3, 4, 5, 6, 7, 8, 7]
repited = 2


#Данный код не решает задачу, если список не отсортирован.
#Возможно удаление элемента внутри цикла и перескакивание через еще не проверенные элементы списка.
#Решение:  проверять только уникальные значения: for each in set(listik)
for each in listik:
    print(each, listik.count(each))
    if listik.count(each) == repited:
        print(each)
        listik.pop(listik.index(each))




print(listik)
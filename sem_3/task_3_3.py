# * Создайте вручную кортеж содержащий элементы разных типов.
# * Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

types_1 = "dsg", "wgt", "gwarg", 1
listik = {}
for each in types_1:
    class_type = type(each).__name__

    # Решение влоб
    # if not listik.get(class_type):
    #     listik[class_type] = []
    # listik[class_type].append(each)

    # Решение получше
    listik.setdefault(class_type, []).append(each)
    # Решение получше
    # listik[class_type] = listik.get(class_type, []) + [each]
print(type(listik), listik)


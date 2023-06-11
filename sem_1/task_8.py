rows = int(input("Введите количество рядов для елки: "))


for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))


print(" " * (rows - 1), end="")

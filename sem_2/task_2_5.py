# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a = 5
b = 8
c = 0

d = b ** 2 - 4 * a * c
print(f"дискриминант = {d}")

x_1 = (-1) * b + d ** 0.5 / 2 * a
x_2 = (-1) * b - d ** 0.5 / 2 * a

print(f"Корни {x_1} {x_2}")

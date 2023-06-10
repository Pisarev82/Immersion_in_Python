def user_input_with_verification(text_to_user):
    while True:
        user_input = input(text_to_user)
        try:
            result = float(user_input)
        except:
            print("введенные данные не являются числом")
            continue
        if result > 0:
            return result

a = user_input_with_verification("Введите длину стороны a: ")
b = user_input_with_verification("Введите длину стороны b: ")
c = user_input_with_verification("Введите длину стороны c: ")

if a >= b + c or b >= a + c or c >= a + b:
    print("Данные длины сторон не образуют треугольник. ")
else:
    if a == b == c:
        print("Эти длины сторон образуют равносторонний треугольник.")
    elif a == b or b == c or c == a:
        print("Эти длины сторон образуют равнобедренный треугольник. ")
    else:
        print("Данные длины сторон образуют разносторонний треугольник.")



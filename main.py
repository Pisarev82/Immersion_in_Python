# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в init пакета имена модулей внутри дандер all
# В модулях создайте дандер all и укажите только те функции, которые могут верно работать за пределами модуля

from sem_6 import my_func, my_func_pro, mystery_dict, show_mystery_guess_dict, validate_date, \
    term_validate_date, find_4_successful_formations

if __name__ == '__main__':
    # my_func(1, 1000, 10)
    # my_func_pro(1, 10, 2)
    # mystery_dict()
    # print(*show_mystery_guess_dict(), sep="\n")
    # print(validate_date("29.02.2000"))
    print(term_validate_date())
    find_4_successful_formations()

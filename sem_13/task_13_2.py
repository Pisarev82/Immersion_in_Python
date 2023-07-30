"""Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений."""

test_dict = {"1": 1, "2": 2}


def my_func(dict, key, default_value):
    try:
        return dict[key]
    except KeyError:
        return default_value

if __name__ == '__main__':

    print(my_func(test_dict, "1", 0))
    print(my_func(test_dict, "3", 0))

"""Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл."""
from json import dump
from math import factorial


class Factorial:

    def __init__(self, k):
        self._k = k
        self.last_factorial = []

    def __call__(self, n):
        result = factorial(n)
        self.last_factorial.append({n: result})
        self.last_factorial = self.last_factorial[-self._k:]
        return result

    def get_history(self):
        return self.last_factorial

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("task_12_2.json", "w") as file:
            dump(self.last_factorial, file, ensure_ascii=True, indent=1)


if __name__ == '__main__':
    with Factorial(5) as a:
        for i in range(6):
            print(a(i))
        print(a.get_history())


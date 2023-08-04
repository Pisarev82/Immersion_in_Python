"""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых. """
import csv
from statistics import mean


class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value[0].isupper():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')
        for character in value:
            if not character.isalpha() and character != ' ':
                raise TypeError(f'Значение {value} должно содержать только буквы')


class Student:
    last_name = Range()
    first_name = Range()
    surname = Range()
    file_name = ""

    def __academic_achievement_from_csv_file(self, file_name):
        self.data = []

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                subject = row[0]
                grade = mean(eval(row[1]))
                test_result = mean(eval(row[2]))
                self.data.append([subject, grade, test_result])

    def __init__(self, last_name, first_name, surname, file_name):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.file_name = file_name
        self.__academic_achievement_from_csv_file(file_name)

    def __repr__(self):
        return f'Student(last_name={self.last_name}, first_name={self.first_name}, ' \
               f'surname={self.surname})'

    def __str__(self):
        result = ""
        for each in self.data:
            result += f"Средний бал по {each[0]} по оценкам {each[1]} по тестам {each[2]} \n"
        return f"Студент: {self.last_name} {self.first_name} {self.surname} \n" \
               f"{result}"


if __name__ == '__main__':
    a = Student("Писарев", "Николай", "Владимирович", "hw_12_1.csv")
    print(a)


"""Ниже приведен код для формирования csv файла"""
    # import csv
    # import random
    #
    # subjects = ['Math', 'Science', 'English', 'History', 'Geography', 'Physics', 'Chemistry', 'Biology',
    #             'Computer Science', 'Art']
    #
    # data = []
    # for subject in subjects:
    #     grade = [random.randint(2, 5) for _ in range(10)]
    #     test_result = [random.randint(0, 100) for _ in range(10)]
    #     data.append([subject, grade, test_result])
    #
    # filename = 'hw_12_1.csv'
    # with open(filename, 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Subject', 'Grade', 'Test Result'])
    #     writer.writerows(data)
    #
    # print(f"Data has been written to {filename}.")
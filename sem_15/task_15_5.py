"""Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
$ python sem_15/task_15_5.py -d 3-й -w вторник -m октября

"""
import datetime

from task_15_4 import convert_to_date, days_of_week, months
import argparse


#Разворот словарей
days_of_week = {key: value for key, value in zip(days_of_week.values(), days_of_week.keys())}
months = {key: value for key, value in zip(months.values(), months.keys())}

def pars_cons_argument():
    parser = argparse.ArgumentParser(description='My first argumentparser')
    parser.add_argument('-d', metavar='d', type=str, default='1-й')
    parser.add_argument('-w', metavar='w', type=str, default=days_of_week[datetime.datetime.now().weekday()])
    parser.add_argument('-m', metavar='m', type=str, default=months[datetime.datetime.now().month])
    args = parser.parse_args()
    result = f'{args.d} {args.w} {args.m}'
    return result


if __name__ == '__main__':
    print(convert_to_date(pars_cons_argument()))


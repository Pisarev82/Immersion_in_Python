"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
import logging
from datetime import datetime

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} {msg}'

logging.basicConfig(filename='D:\\dev\\study\\Immersion _in_Python\\sem_15\\log\\log_4.log', filemode='a',
                    encoding='utf-8', level=logging.ERROR, format=FORMAT, style="{")
logger = logging.getLogger(__name__)

days_of_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}
months = {'января': 1, 'февраля': 2, 'марта': 3,
          'апреля': 4, 'мая': 5, 'июня': 6,
          'июля': 7, 'августа': 8, 'сентября': 9,
          'октября': 10, 'ноября': 11, 'декабря': 12}


def convert_to_date(text_date):
    try:
        # Получаем текущий год
        current_year = datetime.now().year
        # Разбиваем текст на составляющие
        parts = text_date.split()
        # Получаем какой день недели нужно найти
        day_number = int(parts[0].split('-')[0])
        # Получаем номер дня недели
        day_of_week = days_of_week[parts[1]]

        # Получаем номер месяца
        month_number = months[parts[2]]
        # какой день недели 1 число месяца
        curent_weekday_of_month = datetime(current_year, month_number, 1).weekday()
        result_day = 1
        count = 1
        while not (curent_weekday_of_month == day_of_week
                   and count == day_number):
            if curent_weekday_of_month == day_of_week:
                count += 1
            result_day += 1
            try:
                curent_weekday_of_month = datetime(current_year, month_number, result_day).weekday()
            except ValueError as e:
                print(e)
                logger.error(e)

        # Формируем дату с текущим годом
        date = datetime(current_year, month_number, result_day)
        return date
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    text_date = "3-й вторник октября"
    date = convert_to_date(text_date)
    print(date)

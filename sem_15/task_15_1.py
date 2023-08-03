"""Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль."""
import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
'в строке {lineno:03d} функция "{funcName}()" ' \
'в {created} {msg}'
logging.basicConfig(filename='log/log_1.log.', filemode='w',
encoding='utf-8', level=logging.WARNING, format=FORMAT, style="{")
logger = logging.getLogger(__name__)


def division(a, b):
    if b == 0:
        logger.error("Деление на 0")
    else:
        return a/b


division(1, 0)

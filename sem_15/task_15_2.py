"""На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат
"""
import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. в {created} {msg}'
logging.basicConfig(filename='log/log_2.log.', level=logging.INFO,
                    format=FORMAT, style="{", encoding='utf-8')
logger = logging.getLogger(__name__)


def loger_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwars):
        result = func(self, *args, **kwars)
        logger.info(f"функция {func.__name__}() {args= }, {kwars= }, {result= } ")
        return result
    return wrapper


@loger_decorator
def division(a, b):
    if b == 0:
        logger.error("Деление на 0")
    else:
        return a/b


division(1, 0)
division(4, 2)
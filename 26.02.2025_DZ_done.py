# Datetime - импортировать модуль
# На текущем времени вывести все нижеперечисленные методы в консоль
#
# Сдать скриншот#
# datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.
# datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
# datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
# datetime.now(tz=None) - объект datetime из текущей даты и времени.
# datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
# datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
# datetime.strftime(format) - см. функцию strftime из модуля time.
# datetime.date() - объект даты (с отсечением времени).
# datetime.time() - объект времени (с отсечением даты).
# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект
#   datetime с изменёнными атрибутами.
# datetime.timetuple() - возвращает struct_time из datetime.
# datetime.toordinal() - количество дней, прошедших с 01.01.1970.
# datetime.timestamp() - возвращает время в секундах с начала эпохи.
# datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
# datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
# datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
# datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"

import datetime as dt
import time


print(f'datetime.today() - объект datetime из текущей даты и времени = \
{dt.datetime.today()}')
print(f'datetime.fromtimestamp(timestamp) - дата из стандартного представления времени = \
{dt.datetime.fromtimestamp(time.time())}')
print(f'datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970. = \
{dt.datetime.fromordinal(1000)}')
print(f'datetime.now(tz=None) - объект datetime из текущей даты и времени. = \
{dt.datetime.now(tz=None)}')
print(f'datetime.combine(date, time) - объект datetime из комбинации объектов date и time. = \
{dt.datetime.combine(dt.datetime.now(), dt.time())}')
print(f'datetime.strptime(date_string, format) - преобразует строку в datetime = \
{dt.datetime.strptime('23.12.2026', '%d.%m.%Y')}')
print(f'datetime.date() - объект даты (с отсечением времени) = \
{dt.datetime.date(dt.datetime.today())}')
print(f'datetime.time() - объект времени (с отсечением даты). = \
{dt.datetime.time(dt.datetime.today())}')
print(f'datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает \
новый объект datetime с изменёнными атрибутами = \n\t{dt.datetime.today().replace(year=2026)}')
print(f'datetime.timetuple() - возвращает struct_time из datetime. = \n\
    {dt.datetime.today().timetuple()}')
print(f'datetime.toordinal() - количество дней, прошедших с 01.01.1970 = \
{dt.date.today().toordinal()}')
print(f'datetime.timestamp() - возвращает время в секундах с начала эпохи.\
{dt.datetime.timestamp(dt.datetime.today())}')
print(f'datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6 = \
Сегодня {dt.datetime.today().weekday()}-й день недели в США.')
print(f'datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7 = \
Сегодня {dt.datetime.today().isoweekday()}-й день недели в России.')
print(f'datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели) = \
{dt.date.today().isocalendar()}')
print(f'datetime.isoformat(sep=\'T\') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, \
если microsecond == 0, "YYYY-MM-DDTHH:MM:SS" = \
{dt.datetime.today().isoformat()}')

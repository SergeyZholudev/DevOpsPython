# Задание 2.
# Написать функцию is_year_leap, принимающую 1 аргумент — номер года,
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year: int) -> bool:
    '''Leap year check function '''
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

while True:
    try:
        input_year = int(input('Введите год: '))
        if input_year <= 0:
            print('Год не может быть отрицательным или нулевым.')
        else:
            break
    except ValueError:
        print('Введённые данные должны быть числами! Повторите ввод.')

leap_year_checking = is_year_leap(input_year)
print(f'Год {input_year} високосный: {leap_year_checking}')

# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square(side: int) -> tuple:
    """Function for calculating the parameters of a square"""
    func_perimeter = 4 * side
    func_area = side ** 2
    func_diagonal = round(side * math.sqrt(2), 2)
    square_parameters = (func_perimeter, func_area, func_diagonal)
    return square_parameters

(perimeter, area, diagonal) = square(5)
print(f'Периметр квадрата: {perimeter}')
print(f'Площадь квадрата: {area}')
print(f'Диагональ квадрата: {diagonal}')

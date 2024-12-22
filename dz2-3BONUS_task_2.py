# Напишите программу, которая получает от пользователя строку целых чисел, и выводит:
# •	Количество положительных чисел.
# •	Произведение всех отрицательных чисел.
# •	Минимальное и максимальное числа без использования функций min() и max().

while True:
    try:
        inputString = input('Введите последовательность чисел через пробел: ')
        numbers = list(map(int, inputString.split(' ')))  # преобразуем всю введенную последовательность в список чисел
        break
    except ValueError:
        print('Все элементы списка должны быть целыми числами. Повторите ввод.')

# сортировка списка
numbersPositive = []
numbersNegative = []
for num in numbers:
    if num > 0:
        numbersPositive.append(num)
    elif num < 0:
        numbersNegative.append(num)

# Произведение всех отрицательных чисел.
multiplNegative = 1
if len(numbersNegative) != 0:
    for j in numbersNegative:
        multiplNegative *= j
else:
    multiplNegative = len(numbersNegative)

# Минимальное и максимальное числа без использования функций min() и max()
maxNumber = numbers[0]
minNumber = numbers[0]
for num in numbers:
    if num > maxNumber:
        maxNumber = num
    elif num < minNumber:
        minNumber = num

# блок вывода результатов
print(f'Количество положительных чисел = {len(numbersPositive)}')
print(f'Произведение всех отрицательных чисел = {multiplNegative}')
print(f'Максимальное число в списке: {maxNumber}')
print(f'Минимальное число в списке: {minNumber}')

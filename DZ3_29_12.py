# Программа запрашивает ввод, с клавиатуры, целые числа, пока не будет введён 0. Как только будет введён 0 (ноль),
# программа должна посчитать и вывести на экран:
# •	количество введённых чисел (завершающий 0 не считается)
# •	их сумму
# •	среднее арифметическое всех введённых чисел(не считая завершающего числа 0)
# •	определить максимальное и минимальное значение
# •	определить количество чётных и не чётных элементов в последовательности


numbers = []
print('Введите последовательность целых чисел.\nДля завершения введите ноль.')

# блок ввода данных
while True:
    try:
        input_number = int(input('Введите целое число: '))
        if input_number == 0:
            break
        numbers.append(input_number)
    except ValueError:
        print('Введенные величина должна быть целым числом. Повторите ввод.')

# сумма всех чисел
sum_numbers = 0
for num in numbers:
    sum_numbers += num

# среднее арифметическое всех введённых чисел
average_numbers = sum_numbers // len(numbers)

# определить максимальное и минимальное значение
maxNumber = numbers[0]
minNumber = numbers[0]
for num in numbers:
    if num > maxNumber:
        maxNumber = num
    elif num < minNumber:
        minNumber = num

# определить количество чётных и нечётных элементов в последовательности
even_numbers = 0
odd_numbers = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

# блок вывода результатов
print(f'Количество введённых чисел: {len(numbers)}')
print(f'Сумма введённых чисел: {sum_numbers}')
print(f'Максимальное значение введённых чисел: {maxNumber}')
print(f'Минимальное значение введённых чисел: {minNumber}')
print(f'Количество чётных чисел: {even_numbers}')
print(f'Количество нечётных чисел: {odd_numbers}')

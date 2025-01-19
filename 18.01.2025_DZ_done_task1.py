# Задание 1:
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
# произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент: + сложить их;
# -  вычесть; *  умножить; /  разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(num1: int, num2: int, operand: str) -> float|str:
    '''Mathematical operations with 2 numbers'''
    match operand:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return "Неизвестная операция"

while True:
    try:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))
        operator = input("Введите мат.оператор:\n+ сложить их;\n-  вычесть;\n*  умножить;\n/  разделить (первое на второе);\n: ")
        if number2 == 0 and operator == '/':
            print('На ноль делить нельзя. Повторите ввод!')
        else:
            break
    except ValueError:
        print('Введённые данные должны быть числами! Повторите ввод.')

result = arithmetic(number1, number2, operator)
if result == "Неизвестная операция":
    print(result)
else:
    print(f'{number1} {operator} {number2} = {result}')
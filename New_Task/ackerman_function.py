"""
Задача 3: Функция Аккермана
Описание: Напишите программу для вычисления функции Аккермана с помощью
рекурсии. Даны два неотрицательных числа m и n.
"""


def Ackermann(in_num1: int, in_num2: int):
    if in_num1 == 0:
        return in_num2 + 1
    elif in_num1 > 0 and in_num2 == 0:
        return Ackermann(in_num1 - 1, 1)
    elif in_num1 > 0 and in_num2 > 0:
        return Ackermann(in_num1 - 1, Ackermann(in_num1, in_num2 - 1))
    return 0


if __name__ == '__main__':
    num1 = int(input('Введите начальное число: '))
    num2 = int(input('Введите последнее число: '))

    print(Ackermann(num1, num2))
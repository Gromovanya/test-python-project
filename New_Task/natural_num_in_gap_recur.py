"""
Задача 1: Вывод натуральных чисел в промежутке
Описание: Напишите программу, которая выведет все натуральные числа в
промежутке от M до N.
"""

def Print_Range(in_num1: int, in_num2: int, res=''):
    if in_num1 > in_num2:
        return res
    else:
        res += f'{in_num1}, ' if in_num1 < in_num2 else f'{in_num1}'
        return Print_Range(in_num1 + 1, in_num2, res=res)


if __name__ == '__main__':
    num1 = int(input('Введите начальное число: '))
    num2 = int(input('Введите последнее число: '))

    print(Print_Range(num1, num2))
"""
Задача 2: Сумма натуральных элементов в промежутке
Описание: Напишите программу, которая найдёт сумму натуральных элементов в
промежутке от M до N.
"""

def Sum_Range(in_num1: int, in_num2: int, res=0):
    if in_num1 > in_num2:
        return res
    else:
        res += in_num1
        return Sum_Range(in_num1 + 1, in_num2, res=res)

if __name__ == '__main__':
    num1 = int(input('Введите начальное число: '))
    num2 = int(input('Введите последнее число: '))

    print(Sum_Range(num1, num2))
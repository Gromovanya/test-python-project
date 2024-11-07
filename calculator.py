# В этом файле сделан простой калькулятор.
# Где num1 и num2, ты задаешь два значения.
# С ними производятся простые математические действимя.

def calculator(in_num1, in_num2):
    return (f'Сумма - {in_num1 + in_num2}; разность - {in_num1 - in_num2}; '
            f'произведение - {in_num1 * in_num2}; частное - {in_num1 // in_num2};')



if __name__ == '__main__':
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))

    print(calculator(num1, num2))
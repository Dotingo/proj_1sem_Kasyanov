'''
Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
функцией с параметрами. Значения n и m программа должна запрашивать.
'''

def sum(num1, num2): # создаю функцию, в которой выполняется суммирование
    num = 0
    while num1 <= num2: # суммируем числа ряда
        num = num + num1
        num1 = num1 + 1

    return num

def program():
    try:
        n = int(input("Введите первое число: "))
        m = int(input("Введите второе число: "))
        if m < n:
            print("Ошибка ввода")
            program()
        else:
            res = sum(n, m)
            print(res)
    except ValueError:
        print("ошибка ввода")
        program()
program()


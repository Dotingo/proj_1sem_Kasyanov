'''
Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
числу K справа цифру D (D — входной параметр целого тина, лежащий в диапазон
0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу К справа
данные цифры D1 и D2, выводя результат каждого добавления.
'''

def AddRightDigit(D, K):
    K = K * 10 + D #добавляю к числу К цифру D1 и D2
    return K

def program():
    try:
        K = int(input("Введите число K: "))
        D1 = int(input("Введите число от 0 до 9: "))
        D2 = int(input("Введите второе число от 0 до 9: "))
        if 0 <= D1 <= 9 and 0 <= D2 <= 9: # делается проверка значений
            A = AddRightDigit(D1, K)
            print(A)
            print(AddRightDigit(D2, A))
        else:
            print("ошибка ввода")
            program()
    except ValueError:
        print("ошибка ввода")
        program()
program()
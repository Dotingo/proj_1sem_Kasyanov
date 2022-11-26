'''
Дан список размера N. возвести в квадрат все его локальные минимумы.
'''
import random

def program():
    try:
        i = 0
        count = []
        result = []
        N = int(input("Введите размер массива: "))
        lst =[random.randint(0, 100) for _ in range(N)] # создаю лист с рандомными значениями

        print(f"Массив: {lst}")
        for j in range(len(lst) - 1): # делаю цикл, который выводит локальные минимумы
            if lst[j] < lst[j - 1]:
                if lst[j] < lst[j + 1]:
                    count.append(lst[j])
        print(f"Локальные минимумы: {count}")
        print("Локальные минимумы в квадрате:")
        for j in count: # цикл, который выводит минимумы в квадрате
            print(f"{j} = {j**2}")
    except ValueError:
        print("ошибка")
        program()
program()

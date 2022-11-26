'''
Дан список размера N. Найти минимальный из его локальных максимумов.
'''
import random

def program():
    try:
        count = []

        N = int(input("Введите размер массива: "))
        lst =[random.randint(0, 100) for _ in range(N)] # создаю лист с рандомными значениями

        print(f"Массив: {lst}")
        for j in range(len(lst) - 1): # делаю цикл, который выводит локальные максимумы
            if lst[j] > lst[j - 1]:
                if lst[j] > lst[j + 1]:
                    count.append(lst[j])
        print(f"Локальные максимумы: {count}")


        print(f"Минимальный локальный максимум: {min(count)}") # нахожу минимальное число
    except ValueError:
        print("ошибка")
        program()
program()
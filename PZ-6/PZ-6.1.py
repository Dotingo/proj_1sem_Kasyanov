'''
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
нечетные числа в порядке возрастания их индексов, а также их количество К.
'''
import random

def program():
   try:
        i = 0
        count = 0
        list =[]
        while i < 10: # запускаю цикл, который создает лист
            list.append(random.randint(0, 100))
            i += 1
        print(f"Массив: {list}")
        i = 0
        print("Нечетные числа:")
        while i < 10: # запускаю цикл, который выводит нечетные числа
            if list[i] % 2 != 0:
                count += 1
                print(list[i])
            i += 1
        print(f"Количество нечетных чисел: {count}")
   except ValueError:
       print("ошибка")
       program()
program()
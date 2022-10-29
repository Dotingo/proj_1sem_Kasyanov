M = input("напишите массу в килограммах: ") #ожидаем ввод с консоли
while type(M) != int: #цикл обработчик ошибок
    try:
        M = int(M) #строка инпута числом
        tones = M // 1000 #делим M нацело, чтобы узнать количество кг в тоннах
        print(f"{M} килограмм = {tones} тонн")  # выводим на экран
    except ValueError: #при ошибке возобновляем цикл
        print("Введено не число")
        M = input("напишите массу в килограммах: ")
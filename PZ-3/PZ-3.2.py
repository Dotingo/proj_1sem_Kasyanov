def program():
    try:
        num1 = int(input("Номер единицы массы от 1 до 5 \n1 - килограмм \n2 - миллиграмм \n3 - грамм \n4 - тонна \n5 - центнер \n"))
        num2 = int(input("Масса тела: "))


## Нахожу массу тела в килограммах


        if num1 == 1:
            print(num2)
        elif num1 == 2:
            print(num2 / 1000000)
        elif num1 == 3:
            print(num2 / 1000)
        elif num1 == 4:
            print(num2 * 1000)
        elif num1 == 5:
            print(num2 * 100)
        else:
            print("Введено не верное значение")
            program()
    except ValueError:
        print("Введено не верное значение")
program()
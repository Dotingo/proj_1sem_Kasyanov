def program():
    try:
        P = float(input("Введите количество процентов: "))
        fd = 10
        fd = fd + fd / 100 + fd
        if 0 < P < 50:
            tfd = 0
            days = 1
            while tfd <= 200:
                fd += fd / 100 * P
                tfd += fd
                days += 1
            print(f"Количество дней: {days} \nСуммарный пробег: {tfd}")


        else:
            print("Число должно быть от 1 до 50")
            program()

    except ValueError:
        print("ошибка ввода")
        program()


program()

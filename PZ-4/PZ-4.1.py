def program():
    try:
        A = int(input("Введите число А: "))
        B = int(input("Введите число B: "))
        answer = 1


        while A != B:
            A += 1
            answer *= A


        print(answer)

    except ValueError:
        print("ошибка ввода")
        program()

program()
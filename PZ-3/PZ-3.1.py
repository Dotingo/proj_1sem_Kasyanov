def program():
    try:
        A = int(input("введите А: "))
        B = int(input("введите B: "))
        C = int(input("введите C: "))
## проверяю истинность высказывания
        print(A < B < C or A > B >C)

    except ValueError:
        print("Неправильно введены данные")
        program()

program()
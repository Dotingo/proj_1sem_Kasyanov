'''
Туристические агентства предлагают следующие туры. Вояж — Мексика,Канада,Израиль,
Италия, США. РейнаТур — Англия, Япония,Канада, ЮАР. Радуга —- США,Испания, Швеция,
Австралия.
Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США
'''


def program():
    voyage = {
        'name': 'voyage',
        'country': {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'},
    }
    reinaTour = {
        'name': 'reinaTour',
        'country': {'Англия', 'Япония', 'Канада', 'ЮАР'},
    }
    rainbow = {
        'name': 'rainbow',
        'country': {'США', 'Испания', 'Швеция', 'Австралия'},
    }
    allTour = [voyage, reinaTour, rainbow]
    findUsa = []
    findCanada = []

    fullList = voyage['country'] | reinaTour['country'] | rainbow['country']

    for tour in allTour:
        if 'США' in tour['country']:
            findUsa.append(tour['name'])

    for tour in allTour:
        if 'Канада' in tour['country']:
            findCanada.append(tour['name'])

    print(f"Тур в США есть в данных турах: {findUsa}\n Тур в Канаду есть в данных турах: {findCanada}")

program()

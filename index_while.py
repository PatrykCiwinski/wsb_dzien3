lista=[-88,-3,11,23,56,78,98,154,198,275,375,416,524,564,627,738,873,924]

while True:
    liczba=int(input('podaj liczbe do znalezienia: '))
    if liczba in lista:
        print(lista.index(liczba))
        break
    else:
        print('nie ma takiej liczby')
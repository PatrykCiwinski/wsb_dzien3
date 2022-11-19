odp=input("podaj liczbę parzysta  lub Q aby wyjść")


while odp!= 'Q':
    if int(odp)%2==0:
        print('liczba parzysta')
    else:
        print('nie jest parzysta')
        break
    odp=input("podaj liczbę parzysta  lub Q aby wyjść")
else:
    print('Wychodzimy')